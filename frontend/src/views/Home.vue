<template>
  <div class="wrapper">
  <div class="home">
    <h1 class="title">Dark Notes</h1>
    <p class="subtitle"> Welcome to the darkest dark notes </p>
    <input type="text" name="search" class="search" />
  </div>
  </div>
</template>

<script>

export default {
  name: 'home',
}
</script>
<style scoped>
.home {
  position: absolute;
  top:50%;
  left:50%;
  transform: translate(-50%, -50%);

  text-align: center;
  align-content: center;

  display: flex;
  flex-direction: column; 
  width: 50%;
}
.title {
  color: #f35626;
  font-size: 5rem;
  background-image: linear-gradient(92deg, #f35626 0%,#feab3a 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: hue 60s infinite linear; 
  margin: 0;
}
.subtitle {

}
@keyframes hue {
  0% {
    filter: hue-rotate(0deg);
  }
  100% {
    filter: hue-rotate(-360deg);
  }
  
}
</style>
