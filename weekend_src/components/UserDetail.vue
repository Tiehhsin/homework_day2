<template>
    <div>
        This is the information of the student with id: {{$route.params.id }}<br>
        The student's name is: {{$route.params.username}}<br>
        The student's birthday is: {{$route.params.bir}}<br>
    </div>
</template>

<script>
export default {
    name: "UserDetail",
}
</script>

<style scoped>

</style>
