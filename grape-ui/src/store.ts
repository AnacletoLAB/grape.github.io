import { createStore } from "vuex";

export interface State {
  activeVersion: string;
  versions: string[];
}

export const store = createStore<State>({
  state() {
    return {
      activeVersion: "",
      versions: [] as string[],
    } as State;
  },
  mutations: {
    setActiveVersion(state: State, activeVersion: string) {
      if (state.versions.includes(activeVersion)) {
        state.activeVersion = activeVersion;
      } else {
        console.error("Version does not exist");
      }
    },
    setVersions(state: State, versions: string[]) {
      state.versions = versions;
    },
  },
});
