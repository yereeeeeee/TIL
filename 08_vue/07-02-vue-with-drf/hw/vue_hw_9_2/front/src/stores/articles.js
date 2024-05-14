import axios from 'axios'
import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const useArticleStore = defineStore('article', () => {
  const router = useRouter()
  
  const articles = ref([])
  const token = ref(null)
  
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => articles.value = res.data)
  }

  const createArticle = function ({ title, content}) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data: {
        title,
        content
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(res => console.log(res))
  }

  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/signup/',
      data: {
        username, password1, password2
      }
    }).then((res) => {
      console.log('okay')
      const password = password1
      logIn({username, password})
    }).catch((err) => {
      console.log(err)
    })
  }

  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/login/',
      data: {
        username, password
      }
    }).then((res) => {
      token.value = res.data.key
      console.log('login 완료')
      router.push({ name: 'home' })
    }).catch((err) => {
      console.log(err)
    })
  }

  return { articles, token, getArticles, createArticle, signUp, logIn, isLogin }
}, { persist: true })
