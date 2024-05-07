<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <ParentGrandChild :my-msg="myMsg" />
    <button @click="buttonClick">Click me</button>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import ParentGrandChild from '@/components/ParentGrandChild.vue'

  // 내려 받은 props 선언
  // defineProps(['myMsg'])
  defineProps({
    myMsg: String,
    dynamicProps: String
  })

  const emit = defineEmits(['myFocus', 'emitArgs', 'updateName'])

  const buttonClick = function () {
    emit('myFocus')
  }

  const emitArgs = function () {
    emit('emitArgs', 1, 2, 3)
  }

  const updateName = function () {
    emit('updateName')
  }

</script>

<style scoped>

</style>