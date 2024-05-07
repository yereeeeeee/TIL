<template>
  <div style="border: 1px solid lightgray; padding: 0 10px; margin: 10px 0;">
    <h3>자식 페이지입니다.</h3>
    <p>이름 :  {{ childProps.name }}</p>
    <p>나이 :  {{ childProps.age }}</p>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  defineProps({
    childProps: Object
  })

</script>

<style scoped>

</style>