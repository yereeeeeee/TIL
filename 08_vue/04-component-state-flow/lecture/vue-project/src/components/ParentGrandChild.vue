<template>
  <div>
    <p>{{ myMsg }}</p>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  defineProps({
    myMsg: String
  })

</script>

<style scoped>

</style>