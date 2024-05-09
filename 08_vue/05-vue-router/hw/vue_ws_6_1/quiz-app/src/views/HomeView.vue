<template>
  <div class="container" style="margin-top: 20px;">
    <h3>퀴즈 앱 사용 방법</h3>
    <div class="rule-wrap" id="quiz1">
      <div>
        <h1>1. 퀴즈 목록 확인하기</h1>
        <br>
        <p>퀴즈 목록 페이지에서 다양한 퀴즈를 확인하세요.</p>
        <div class="img-wrap shadow">
          <img src="../assets/quizList.png" alt="" class="example-img">
        </div>
      </div>
    </div>
    <div class="rule-wrap" id="quiz2">
      <div>
        <h1>2. 퀴즈 생성하기</h1>
        <br>
        <p>퀴즈는 직접 생성 할 수도 있어요.</p>
        <div class="img-wrap shadow">
          <img src="../assets/quizCreate.png" alt="" class="example-img">
        </div>
      </div>
    </div>
    <div class="rule-wrap" id="quiz3">
      <div>
        <h1>3. 정답 페이지</h1>
        <br>
        <p>작성한 답변이 정답인지 확인하세요.</p>
        <div class="img-wrap shadow">
          <img src="../assets//quizAnswer.png" alt="" class="example-img">
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  

</script>

<style scoped>
  .rule-wrap {
    margin-top: 50px;
  }
  .example-img {
    width: 100%;
  }
  .img-wrap {
    border: 1px solid lightgray;
    padding: 5px
  }

</style>