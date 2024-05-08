<template>
  <div>
    <h1>학생 상세 정보 목록입니다.</h1>
    <ul>
      <p v-for="student in students">
        <RouterLink :to="{ name: 'studentsDetail', params: { 'name': student.name }}" style="text-decoration: none; color: black;">{{ student.name }} 학생 정보 보기</RouterLink>
      </p>
    </ul>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  
  const students = ref([
    {id: 1, name: '김하나'},
    {id: 2, name: '김두리'},
    {id: 3, name: '김서이'},
  ])


</script>

<style scoped>

</style>