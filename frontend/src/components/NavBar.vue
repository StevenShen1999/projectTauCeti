<template>
<div class="wrapper">
    <div class="logo">
        <router-link to="/"><h1>Dark Notes</h1></router-link>
    </div>
    <div class="search">
        <input type="text" name="search" />
    </div>
    <div class="user">
        <div v-if="login">
        <router-link to="/logout" class="fas fa-user"></router-link>
        </div>
        <div class="login" v-else>
            <router-link class="primary" to="/login">Log in</router-link>
        </div>
    </div>
    
</div>
    
</template>
<style lang="scss" scoped>
.wrapper {
    height: 90px;
    background-color: white;
    display: flex;
    justify-content: space-between;
    align-content: center;
}
.logo {
    margin-left: 20px;
  & h1 {
    color: #f35626;
    font-size: 2rem;
    background-image: linear-gradient(92deg, #f35626 0%,#feab3a 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: hue 60s infinite linear; 
  }
}
@keyframes hue {
  0% {
    filter: hue-rotate(0deg);
  }
  100% {
    filter: hue-rotate(-360deg);
  }
  
}
.search {
    margin: auto 0;
    width: 40%;
    max-width: 500px;
    & input {

        border-radius: 30px;
        background-color: #eee;
        border: none;
        padding: 12px 15px;
        margin: 8px 0;
        width: 100%;
        width: 100%;
    }
}
.user {
    font-size: 2rem;
    margin: auto 10px;
}
.login {
    display: flex;
    & .primary {
        color: black;
        margin-left: 5px;
        font-size: 0.6em;
        padding: 2px 10px;
    }
    & .secondary {
        color: black;
        margin-left: 5px;
        font-size: 0.6em;
        padding: 2px 10px;
    }
}

</style>
<script>
export default {
    data: () => ({
        login: false 
    })
}
</script>