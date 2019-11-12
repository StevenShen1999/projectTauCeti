<template>
    <div class="course-wrapper"> 
    <NavBar/>
    <div class="course-container">
        <div class="main">
            <div class="files"><CourseHome /></div>   
            <div class="chat"><Chat /> </div>   
        </div>
    </div>
    </div>
</template>
<script>
import NavBar from '@/components/NavBar.vue'
import CourseHome from '@/components/CourseHome.vue'
import Chat from '@/components/Chat.vue'
export default {
    name: "course",
    props: ["cid"],
    components: {NavBar,CourseHome, Chat}
}
</script>
<style lang='scss' scoped>
.course-wrapper {
    position: absolute;
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-items: stretch;
}
.course-container {
    position: relative;
    height: 100%;
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
    overflow-x: hidden;
    height: 100%;
    flex: 4 1 0;
    position: relative;
    background-color: white;
}
.chat {
    overflow: scroll;
    overflow-x: hidden;
    flex: 2 1 0;
    height: 100%;
    position: relative;
    background-color: #E8E4B3;
}

</style>