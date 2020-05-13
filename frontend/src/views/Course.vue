<template>
    <v-app>
        <CourseChat />
        <CourseMenu v-model="model" :items="items"/>
        <v-content> 
        <v-fade-transition
        hide-on-leave
        >
        <CourseHome v-if="model == 0"/>
        </v-fade-transition>
        <CourseOutline  v-if="model == 1"/>
        <CourseNotes  v-else-if="model == 2"/>
        </v-content>
    </v-app>

                

            

    
</template>
<script>
import CourseChat from '@/components/Course/CourseChat.vue'
import CourseMenu from '@/components/Course/CourseMenu.vue'
import CourseOutline from '@/components/Course/CourseOutline.vue'
import CourseNotes from '@/components/Course/CourseNotes.vue'
import CourseHome from '@/components/Course/CourseHome.vue'
export default {
    name: "Course",
    components: {
        CourseChat, CourseOutline, CourseMenu, CourseNotes, CourseHome
    },
    data: () => {
        return {
        items: [
            {
            icon: 'home',
            title: 'Home'
            },
            {
            icon: 'info',
            title: 'Course Information'
            },
            {
            icon: 'list',
            title: 'Notes'
            },
        ],
        model:  0
        }
    }
}
</script>
<style lang="scss" >

</style>