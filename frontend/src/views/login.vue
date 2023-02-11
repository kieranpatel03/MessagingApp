<template>
    <form @submit.prevent="form_submit">
        <div class="form-inputs">
            <div v-if="user_not_exists">
                <h4 style="color: red; text-align: center">That User Does Not Exist!</h4>
            </div>
            <div class="form-input">
                <label for="username">Enter Username:</label>
                <br/>
                <input type="text" name="username" v-model="username"/>
            </div>
            <div class="form-input">
                <label for="password">Enter Password:</label>
                <br/>
                <input type="password" name="password" v-model="password"/>
            </div>
            <div class="form-input">
                <input type="submit" value="Login"/>
            </div>
        </div>
    </form>
</template>

<script>

export default {
    name: 'LoginPage',
    data() {
        return {
            username: '',
            password: '',
            user_not_exists: false,
        }
    },
    methods: {
        form_submit() {
            const body_msg = JSON.stringify({username: this.username, password: this.password})
            fetch('http://127.0.0.1:8000/retrieve', {
                method: "POST",
                headers: {
                    "Content-type": "application/json",
                }, 
                body: body_msg,
            }).then(
                    data => {if (data.status == 422){
                        this.user_not_exists = true;
                        this.username = '';
                        this.password = '';
                    } else if (data.status == 200){
                        data.json().then(
                            data => {
                                this.$cookies.set('token', data['token'])
                                this.$router.push('/').then(() => { this.$router.go() })
                            }
                        )
                    }
            })
        }
    }
}

</script>

<style>

form {
    position: relative
}

.form-inputs {
    position: absolute;
    left: 43%;
}

.form-input {
    margin: 30px;
}

</style>