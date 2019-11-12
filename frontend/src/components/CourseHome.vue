<template>
    
    <div class="container">
        <div class="about">
            <h1> COMP1511 </h1>
            <p> The bEsT first year course </p> 
            <img src="https://i.imgur.com/5S42Lyr.jpg"/>
        </div>
        <Notes/>
    </div>
</template>
<script>
import Notes from '@/components/Notes'
export default {
    components: {
        Notes
    }
    
}
</script>
<style lang="scss" scoped>
.container {
    margin: 0 20px;
}
.about {
    & img {
        max-width: 100%;
    }
}
</style>