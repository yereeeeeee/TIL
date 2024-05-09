<template>
  <div class="bigger-box">
    <h2 style="margin-bottom: 10px;">부모 컴포넌트</h2>
    <p class="family">{{ family.father }}</p>
    <p class="family">{{ family.mother }}</p>
    <div class="child-box">
      <ChildPage 
        v-for="child in family.children"
        :child="child"
      />
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import ChildPage from './ChildPage.vue';

  defineProps ({
    family: Object
  })

</script>

<style scoped>
  .bigger-box {
    background-color: rgb(245, 245, 245); 
    border: 1px lightgray solid;
    width: 80%;
    text-align: center;
    padding: 20px 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
  }
  .child-box {
    /* justify-content: center; */
    align-items: center;
    width: 90%;
    display: flex;
    flex-direction: column;
  }
  .family {
    margin: 3px 0;
  }
</style>