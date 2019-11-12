<template>
  <div id="app">
    <transition name="fade">
      <router-view/>
    </transition>
  </div>
</template>

<style>
@import url(https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css);
@import url('https://fonts.googleapis.com/css?family=Raleway&display=swap');
* {
  box-sizing: border-box;
}
body {
  font-family: Raleway,Helvetica,Arial,sans-serif;
  margin: 0;
}
input {
  outline :none;
}
a {
  text-decoration: none;
}
::-webkit-scrollbar {
  display: none;
}

::-webkit-scrollbar-track {
display: none;
}
 
#app {
  display: absolute;
  width: 100%;
  height: 100%;;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
