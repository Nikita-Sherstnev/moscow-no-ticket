<template>
  <div class="container">
    <div class="schema-wrapper">
      <img src="../assets/schema_1.png" alt="Schema" class="schema" />
      <img src="../assets/schema_2.png" alt="Schema" class="schema" />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Schema",
});
</script>

<style lang="scss">
.container {
  position: relative;
  width: 100%;
  height: 100%;
}

.schema-wrapper {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.schema {
  position: relative;
  width: 100%;
  height: 100%;
  user-select: none;
}
</style>
