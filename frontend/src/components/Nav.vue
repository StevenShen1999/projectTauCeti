<template>
<div class="nav-wrapper">
    <router-link to="/" class="fas fa-home"></router-link>
    <router-link to="/course" class="fas fa-list-ul"></router-link>
    <router-link to="/course" class="fas fa-trophy"></router-link>
</div>
    
</template>
<script>
export default {
    
}
</script>
<style scoped>
@import url(https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css);
.nav-wrapper {
    position: relative;
    width: 100%;
    height: auto;
    max-height: 100%;
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: flex-start;
    align-items: flex-start;
}
a {
    margin: 10px auto;
    font-size: 2rem;
    text-decoration:none ;
    color: black;
}


</style>