<template>
    <div class="wrapper"> 
        <div class="left"><Nav/> </div>   
        <div class="main">
            <div class="files"><CourseHome /></div>   
            <div class="chat"><Chat /> </div>   
        </div>
    </div>
</template>
<script>
import Nav from '@/components/Nav.vue'
import CourseHome from '@/components/CourseHome.vue'
import Chat from '@/components/Chat.vue'
export default {
    name: "course",
    props: ["cid"],
    components: {Nav,CourseHome, Chat}
}
</script>
<style lang='scss' scoped>
.wrapper {
    position: absolute;
    height: 100%;
    width: 100%;
    display: flex; 
}
.left {
    flex-grow: 0;
    min-height: 100%;
    background-color: #FAFFD1;
    width: 50px;
    position: relative;
}
.main {
    height: 100%;
    width: 100%;
    position: relative;
    display: flex; 
}
.files {
    overflow: scroll;
    height: 100%;
    flex: 4 1 0;
    position: relative;
    background-color: white;
}
.chat {
    overflow: scroll;
    flex: 2 1 0;
    height: 100%;
    position: relative;
    background-color: #E8E4B3;
}

</style>