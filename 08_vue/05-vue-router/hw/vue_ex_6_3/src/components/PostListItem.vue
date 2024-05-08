<template>
  <div>
    <p>
      {{ post.id }}. <RouterLink :to="{ name: 'post-detail', params: { 'id': post.id } }">제목 : {{ post.title }}</RouterLink>
    </p>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { RouterLink } from 'vue-router';
  
  defineProps({
    post: Object,
  })

</script>

<style scoped>

</style>