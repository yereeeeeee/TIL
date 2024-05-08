<template>
  <div>
    <p>번호 : {{ posts[postId-1].id }}</p>
    <p>제목 : {{ posts[postId-1].title }}</p>
    <p>내용 : {{ posts[postId-1].content }}</p>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useRoute, onBeforeRouteUpdate } from 'vue-router'

  const route = useRoute()
  const postId = ref(route.params.id)

  const posts = ref([
    { id: 1, title: '제목 1', content: '내용 1' },
    { id: 2, title: '제목 2', content: '내용 2' },
    { id: 3, title: '제목 3', content: '내용 3' },
  ])

onBeforeRouteUpdate((to, from) => {
  postId.value = to.params.id
})
</script>

<style scoped>

</style>