<template>
  <div class="container">
    <div class="container-avatar">
      <img src="../assets/rabbit_1.png" class="rabbit" />

      <!--      <img src="../assets/face.png" class="face" />-->
      <img :src="source" class="face" />
    </div>
    <div class="date">Дата</div>
    <div class="stars">
      <star />
      <star />
      <star />
      <star />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";
import { Box } from "@/types";
import Star from "@/components/Star.vue";

export default defineComponent({
  name: "Card",
  components: { Star },
  props: {
    source: {
      type: String,
      required: true,
    },
    box: {
      type: Object as PropType<Box>,
      required: true,
    },
  },
});
</script>

<style scoped lang="scss">
.container {
  width: 450px;
  height: auto;
  box-sizing: border-box;
  color: white;
  user-select: none;
}

.container-avatar {
  width: 450px;
  height: 450px;
  border-radius: 50%;
  box-sizing: border-box;
  position: relative;
  background: transparent; //#f5f5f5;
}

.rabbit {
  position: absolute;
  top: 0;
  left: calc(50% - 130px);
  height: 100%;
  width: auto;
  z-index: 100;
}

.face {
  position: absolute;
  top: 210px;
  left: 180px;
  width: 80px;
  height: 80px;
  z-index: 1;
}
</style>
