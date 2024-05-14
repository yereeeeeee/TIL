<template>
  <div>
    <header>
      <h1>My Gallery</h1>
    </header>

    <main>
      <div class="container">
        <div class="row gy-4">
          <div class="col xs-12 sm-6 md-4 card_wrap" v-for="_ in numberOfItems">
            <div class="card" style="width: 18rem;">
              <img src="@/assets/sample.png" class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const numberOfItems = ref(4)
</script>

<style scoped>
header {
  background-color: rgb(207, 241, 231);
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  text-align: center;
}

main {
  margin-top: 80px;
}

.card_wrap {
  display: flex;
  justify-content: center;
}

</style>
