<template>
  <div class="comtainer">
    <h1>Todos</h1>
    <div class="alert alert-success alert-dismissible fade show" role="alert">
      Бутстрап подключен и работает
      <button type="button" class="close" data-dismiss="alert" aria-lebel="Close">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    <p>{{ msg }}</p>
    <table>
      <thead>
      <tr>
        <th>Uid</th>
        <th>Описание</th>
        <th>Выполнена?</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="(todo,index) in todos" :key="index">
        <td>{{ todo.uid }}</td>
        <td>{{ todo.description }}</td>
        <td>
          <span v-if="todo.is_completed">Выполнено</span>
          <span v-else>Не выполнено</span>
        </td>
      </tr>
      </tbody>
    </table>
   </div>
</template>

<script>
import axios from 'axios';

const dataURL = 'http://localhost:5000/api/tasks/';

export default {
  name: 'Fetch',
  data() {
    return {
      todos: [],
    };
  },
  methods: {
    getMessage() {
      axios.get(dataURL)
        .then((response) => {
          // console.table(response.data.tasks);
          this.todos = response.data.tasks;
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
