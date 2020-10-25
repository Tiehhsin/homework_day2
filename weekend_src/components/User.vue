<template>

    <div>
        这是User组件
        <h3>用户列表页</h3>
        <table border="2">
            <tr>
                <td>ID</td>
                <td>姓名</td>
                <td>生日</td>
                <td>个人信息</td>
                <td>操作</td>
            </tr>
            <tr v-for="(user,id) in users" :key="user.id">
                <td>{{ user.id }}</td>
                <td>{{ user.username }}</td>
                <td>{{ user.bir }}</td>
                <td>{{ user.content }}</td>
                <td><a href="javascript:;" @click="rem(id)">删除</a>  |
                    <router-link :to="`/detail/${user.id}&${user.username}&${user.bir}`">查看用户详情</router-link>
                </td>
            </tr>
        </table>

        <hr>
        用户名: <input type="text" v-model="username"><br>
        生日: <input type="text" v-model="bir"><br>
        个人信息: <input type="text" v-model="content"><br>
        <button @click="addUser">添加用户</button>

    </div>

</template>

<script>
export default {
    name: "User",
    data() {
        return {
            users:localStorage.plist ? JSON.parse(localStorage.plist) :
            [
                {"id": 1, username: "Andy", bir: "1999-01-01", content: 'I am Andy'},
                {"id": 2, username: "Jason", bir: "2000-02-12", content: 'I am Jason'},
                {"id": 3, username: "Jared", bir: "1998-11-12", content: 'I am Jared'},
            ],

            // users:[
            //     {"id": 1, username: "Andy", bir: "1999-01-01", content: 'I am Andy'},
            //     {"id": 2, username: "Jason", bir: "2000-02-12", content: 'I am Jason'},
            //     {"id": 3, username: "Jared", bir: "1998-11-12", content: 'I am Jared'},
            // ],
            username: "",
            bir: "",
            content: "",
            id:0,
        }
    },
    methods: {
        addUser() {
            // 获取到三个用户信息
            this.users.push({'id':this.users.length+1,username:this.username,bir:this.bir,content:this.content})
            this.username = ''
            this.bir = ''
            this.content = ''

            localStorage.plist=JSON.stringify(this.users)
        },
        rem(id){
            this.users.splice(id,1)
            localStorage.plist=JSON.stringify(this.users)

        },

    },
}
// localStorage.clear()
</script>


<style scoped>

</style>
