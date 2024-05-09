<template>
  <div class="box">
    <h3>자식 페이지</h3>
    <p>{{ child.name }}</p>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  
  defineProps({
    child: Object
  })

</script>

<style scoped>
  .box {
    text-align: center;
    border: 1px solid lightgray;
    width: 100%;
    margin: 5px 0;
    background-color: white;
  }
</style>