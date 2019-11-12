<template>
<div>
        <h1>Notes for COMP 1511</h1>
        <div class="file-list">
            <ol>
                <li v-for="(file, index) in files" :key="file.id"  class="file">
                    <div class="file_summary" @click="select(index)">
                    <span class="file_summary_index">#{{index + 1}}</span>
                    <span class="file_summary_title">{{file.title}}</span>
                    </div>
                    <transition name="details">
                        <div v-if="selected == index" class="file_content"> 
                            <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/344846/_jung.jpg" />
                            <p>
                                The Swiss psychologist and psychiatrist Carl Jung was one of the major forces responsible for bringing psychological (having to do with the mind and its processes) thought and its theories into the twentieth century.
                            </p>
                        </div>
                    </transition>
                </li>
            </ol>
        </div>
    </div>
</template>
<script>
export default {
    mounted() {
    },
    data: () => ({
        files: [
            {
                id: 2,
                title: "COMP1511, basics of googling and stack overflow"
            },
            {
                id: 1,
                title: "Introduction to C and Linux all you need"
            },
        ],
        selected: -1
    }),
    methods: {
        select: function(index)  {
            this.selected = index == this.selected ? -1 : index;
        }
    }
}
</script>
<style lang='scss' scoped>
ol {
    margin: 0;
    padding: 0;
}
li {
    display: block;
}
.file {
    &:hover {
        background-color: #fafafa;
        & .file_summary {
            cursor: pointer;
            &_title {
            }
            &_index {
                opacity:0.5;
            }
        }
    }
    &_summary {
        display: flex;
        align-content: center;
        justify-content: flex-start;
        text-align: left;
        position: relative;
        min-height: 4rem;
        &_index {
            position: relative;
            margin: auto 0;
            font-size:5rem;
            font-weight:bold;
            color:black;
            opacity:0.1;
            transition:0.25s;
        }
        &_title {
            left: 1rem;
            margin: auto 0;
            position: relative;
            transition: all 0.25s;

        }
    }
    &_content {
        display: flex;
        flex-wrap: wrap;
        overflow: hidden;
        flex-direction: row;
        justify-content: center;
        padding: 0 20px;
        line-height: 1.5; 
        max-height: 500px;
        user-select: none;
        & img {
            object-fit: scale-down;
            position: relative;
            max-height: 80vh;
            max-width: 100%;
            margin-top: 20px;
        }
        & p {
            flex: 1;
        }
    }
}
.details-enter-active {
    animation: slideDown .5s;
}
@keyframes slideDown {
  from {
    opacity: 0;
    max-height: 0;
  }

  to {
    opacity: 1;
    max-height: 500px;
  }
}
</style>