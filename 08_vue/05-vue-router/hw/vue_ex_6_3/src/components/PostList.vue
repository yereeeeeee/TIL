<template>
  <div>
    <h2>{{ $route.params.username }}이 작성한 게시글</h2>
    <ul v-for="post in posts">
      <PostListItem 
        :post=post
      />
    </ul>
  </div>
  <hr>
  <RouterView />
</template>

<script setup>
  import { ref } from 'vue'
  import { RouterView } from 'vue-router';
  import PostListItem from './PostListItem.vue'
  
  const posts = ref([
    { id: 1, title: '제목 1', content: '내용 1' },
    { id: 2, title: '제목 2', content: '내용 2' },
    { id: 3, title: '제목 3', content: '내용 3' },
  ])

</script>

<style scoped>

</style>