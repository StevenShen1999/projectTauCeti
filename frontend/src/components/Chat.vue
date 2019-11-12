<template>
    <div class="wrapper">
        <div class="header" >
        </div>
        <div class="messages">
            <p :class="index % 2 ? 'left' : 'right'" v-for="(message, index) in messages" :key="index">{{message}}</p>
        </div>
        <div class="input">
            <form @submit="sendMessage">
            <input v-model="messageEntered" type="text" name="message"/>
            </form>
        </div>
        
    </div>
</template>
<script>
export default {
    data: () => ({
        messages: [
            "If you have one bucket that contains 2 gallons and another bucket that contains 7 gallons, how many buckets do you have?",
            "Stfu"
        ], 
        messageEntered: ''
    }),
    methods: {
        sendMessage: function(e ) {
            e.preventDefault()
            this.messages.push(this.messageEntered)
            this.messageEntered = ""
        }
    }
}
</script>
<style lang="scss" scoped>
.wrapper {
    display: flex;
    width: 100%;
    position: relative;
    flex-direction: column;
    align-items: stretch;
}
.header {
    background-color: black;
    height: 7vh;
    flex-grow: 0;
}
.messages {
    flex-grow: 1;
    position: relative;
    display: flex;
    flex-direction: column;
}
.left {
    margin-left: 10px;
}
.right {
    margin-right: 10px;
}
p {
    flex-grow: 0;
	// layout
	position: relative;
	
	// looks
	background-color: #fff;
	padding: 1.125em 1.5em;
	border-radius: 1rem;
  box-shadow:	0 0.125rem 0.5rem rgba(0, 0, 0, .3), 0 0.0625rem 0.125rem rgba(0, 0, 0, .2);
}

.right::before, .left::before {
	// layout
	content: '';
	position: absolute;
	width: 0;
	height: 0;
	top: 100%;
	border: .75rem solid transparent;
	border-bottom: none;

	// looks
	border-top-color: #fff;
	filter: drop-shadow(0 0.0625rem 0.0625rem rgba(0, 0, 0, .1));
}
.left::before {
	left: 1.5em; // offset should move with padding of parent
}
.right::before {
    right: 1.5em;
}
.input {
    position: relative;
    & form {
        position: relative;
    }
    & input {
        width: 100%;
        padding: 1em 1.5em;
        border: none;
    }
}

</style>