<template>
  <div>
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ childProps.name }}</p>
    <p>나이 : {{ childProps.age }}</p>
    <p>용돈 : {{ childProps.balance }}</p>
    <!-- <form @submit.prevent="giveMeAllowance">
      <input type="submit" value="hi">
    </form> -->
    <button @click="giveMeAllowance">용돈 주세요.</button>
  </div> 
</template>

<script setup>
  import { ref } from 'vue'
  defineProps({
    childProps: Object
  })

  const emit = defineEmits(['updateBalance'])

  const giveMeAllowance = function() {
    emit('updateBalance')
  }

</script>

<style scoped>

</style>