<template>
  <div class="container">
    <h1>Quiz Développements Limités</h1>

    <div v-if="loading">Chargement...</div>

    <div v-else>

      <div class="question">
        <p>{{ questionText }}</p>
        <div v-html="renderLatex(questionLatex)"></div>
      </div>

      <div class="answers">
        <button
          v-for="(answer, index) in answers"
          :key="index"
          @click="checkAnswer(answer)"
          :class="getButtonClass(answer)"
          :disabled="answered"
          v-html="renderLatex(answer)"
        ></button>
      </div>

      <div v-if="answered" class="result">
        <p v-if="selectedAnswer === correctAnswer">Bonne réponse !</p>
        <p v-else>Mauvaise réponse</p>

        <button @click="loadQuestion">Question suivante</button>
      </div>

      <div class="score">
        Score : {{ score }}
      </div>

    </div>
  </div>
</template>

<script>
import axios from "axios"
import katex from "katex"
import "katex/dist/katex.min.css"

export default {
  data() {
    return {
      questionText: "",
      questionLatex: "",
      answers: [],
      correctAnswer: "",
      selectedAnswer: null,
      answered: false,
      score: 0,
      loading: true
    }
  },

  mounted() {
    this.loadQuestion()
  },

  methods: {

    async loadQuestion() {
      this.loading = true
      this.answered = false
      this.selectedAnswer = null

      const response = await axios.get("http://127.0.0.1:8000/question")

      this.questionText = response.data.question_text
      this.questionLatex = response.data.question_latex
      this.answers = response.data.answers
      this.correctAnswer = response.data.correct_answer

      this.loading = false
    },

    checkAnswer(answer) {
      this.selectedAnswer = answer
      this.answered = true

      if (answer === this.correctAnswer) {
        this.score++
      }
    },

    getButtonClass(answer) {
      if (!this.answered) return ""

      if (answer === this.correctAnswer) return "correct"
      if (answer === this.selectedAnswer) return "wrong"

      return ""
    },

    renderLatex(text) {
      try {
        return katex.renderToString(text, {
          throwOnError: false,
          displayMode: true
        })
      } catch (e) {
        return text
      }
    }

  }
}
</script>

<style>
.container {
  max-width: 800px;
  margin: auto;
  text-align: center;
  font-family: Arial;
}

.question {
  margin: 30px 0;
  font-size: 20px;
}

.answers button {
  display: block;
  width: 100%;
  margin: 10px 0;
  padding: 12px;
  font-size: 16px;
  cursor: pointer;
}

.correct {
  background-color: #4CAF50;
  color: white;
}

.wrong {
  background-color: #f44336;
  color: white;
}

.result {
  margin-top: 20px;
}

.score {
  margin-top: 20px;
  font-weight: bold;
}
</style>