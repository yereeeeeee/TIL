<template>
  <div>
    <form @submit.prevent="createTodo(todoText)" ref="formElem">
      <input type="text" v-model="todoText">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useCounterStore } from '@/stores/counter';

  const store = useCounterStore()
  
  const todoText = ref('')
  const formElem = ref(null)

  const createTodo = function() {
    if (todoText.value.trim()) {
      store.addTodo(todoText.value)
      formElem.value.reset()
      todoText.value = ''
    }
  }

  

</script>

<style scoped>

</style>