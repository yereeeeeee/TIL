<template>
  <div style="padding: 0 5%;">
    <div v-for="article in store.articles">
      <h3>{{ store.articles.indexOf(article) + 1 }} 번 게시글</h3>
      <p>제목 : {{ article.title }}</p>
      <p>내용 : {{ article.content }}</p>
      <hr>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/articles'
const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})
</script>

<style lang="scss" scoped>

</style>