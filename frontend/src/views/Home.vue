<template>
  <div class="wrapper">
    <div class="login"> 
          <router-link class="primary" to="/login">Log in</router-link>
      </div>
  <div class="home">
    <h1 class="title">Dark Notes</h1>
    <p class="subtitle"> Welcome to the darkest dark notes </p>
    <input type="text" name="search" class="search" placeholder="Search your course here"/>
  </div>
  </div>
</template>

<script>

export default {
  name: 'home',
}
</script>
<style lang="scss" scoped>
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
.login {
  position: absolute;
  top: 10px ;
  right: 10px;
    & a {
        color: black;
        margin-left: 5px;
        font-size: 1.2rem;
        padding: 2px 10px;
    }
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
.search {
    margin: auto 0;
    width: 100%;
    border-radius: 30px;
    background-color: #eee;
    border: none;
    padding: 12px 15px;
    margin: 8px 0;
    width: 100%;
    width: 100%;
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
