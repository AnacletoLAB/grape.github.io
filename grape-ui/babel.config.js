module.exports = {
  presets: ["@vue/cli-plugin-babel/preset"],
  exclude:
    process.env.NODE_ENV === "production"
      ? [
          "**/src/mocks/**", // ignore the whole test directory, probably not working
        ]
      : [],
};
