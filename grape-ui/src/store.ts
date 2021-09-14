import { createStore } from "vuex";

export interface State {
  test: string;
}

export const store = createStore<State>({
  state() {
    return {
      test: "" as string,
    };
  },
  mutations: {},
});
