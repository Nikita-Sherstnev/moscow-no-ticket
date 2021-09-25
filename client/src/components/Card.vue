<template>
  <div class="container">
    <div class="status-bar">
      <div class="stars">
        <star v-for="i in rating" :key="i" />
      </div>
      <div class="date">{{ date }}</div>
    </div>
    <div class="container-avatar">
      <img src="../assets/rabbit_2.png" class="rabbit" />

      <div class="face-wrapper">
        <div class="face-zoom" :style="{ transform: `scale(${coords.scale})` }">
          }
          <img
            :src="`data:image/png;base64, ${source}`"
            class="face"
            :style="{
              top: coords.top,
              left: coords.left,
            }"
            alt="Face"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, PropType } from "vue";
import { Box } from "@/types";
import Star from "@/components/Star.vue";

type CustomBox = {
  x: number;
  y: number;
  w: number;
  h: number;
};

type Coords = {
  top: string;
  left: string;
  scale: string;
};

export default defineComponent({
  name: "Card",
  components: { Star },
  props: {
    source: {
      type: String,
      required: true,
    },
    rect: {
      type: Object as PropType<number[]>,
      required: true,
    },
    date: {
      type: String,
      required: true,
    },
    rating: {
      type: Number,
      required: true,
    },
  },
  setup(props) {
    const box = computed<CustomBox>(() => {
      return {
        y: props.rect[0],
        x: props.rect[1],
        h: props.rect[2] - props.rect[0],
        w: props.rect[3] - props.rect[1],
      };
    });

    console.log((box.value, box.value.w / 2));

    const coords = computed<Coords>(() => {
      return {
        top: `-${box.value.x - 75 + box.value.h / 2}px`,
        left: `-${box.value.y - 200 + box.value.w / 2}px`,
        scale: `${250 / (box.value.w * 2)}`, //${250 / box.value.w}
      };
    });

    return {
      box,
      coords,
    };
  },
});
</script>

<style scoped lang="scss">
.container {
  width: 600px;
  height: auto;
  box-sizing: border-box;
  color: white;
  user-select: none;
  position: relative;
}

.status-bar {
  position: absolute;
  z-index: 1000;
  top: 0;
  left: calc(50% - 150px);
  width: 300px;
  height: auto;
  background: rgba(#fff, 0.25);
  border-radius: 30px;
  border: 3px solid rgba(#000, 0.2)
}

.date {
  text-shadow: 1px 2px 0 #000;
  font-size: 32px;
}

.container-avatar {
  width: 600px;
  height: 600px;
  border-radius: 50%;
  box-sizing: border-box;
  position: relative;
  background: transparent; //#f5f5f5;
}

.rabbit {
  position: absolute;
  top: -320px;
  left: calc(50% - 300px);
  height: auto;
  width: 100%;
  z-index: 100;
}

.face-wrapper {
  clip-path: circle(50% at 50% 50%);
  position: absolute;
  top: 300px;
  left: 90px;
  width: 400px;
  height: 150px;
  z-index: 1;
}

.face-zoom {
  clip-path: circle(50% at 50% 50%);
  width: 400px;
  height: 150px;
}

.face {
  position: absolute;
  z-index: 1;
}
</style>
