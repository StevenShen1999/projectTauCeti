<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style>
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
</style>
