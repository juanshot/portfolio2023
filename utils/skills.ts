export interface Tech {
  name: string;
  icon: string;
}

export interface TechGroup {
  key: string;
  items: Tech[];
}

export const skillGroups: TechGroup[] = [
  {
    key: "languages",
    items: [
      { name: "JavaScript", icon: "simple-icons:javascript" },
      { name: "TypeScript", icon: "simple-icons:typescript" },
      { name: "PHP", icon: "simple-icons:php" },
      { name: "Go", icon: "simple-icons:go" },
      { name: "HTML5", icon: "simple-icons:html5" },
      { name: "CSS3", icon: "simple-icons:css" },
      { name: "Sass", icon: "simple-icons:sass" },
    ],
  },
  {
    key: "frontend",
    items: [
      { name: "Vue.js", icon: "simple-icons:vuedotjs" },
      { name: "Nuxt", icon: "simple-icons:nuxt" },
      { name: "React", icon: "simple-icons:react" },
      { name: "Next.js", icon: "simple-icons:nextdotjs" },
      { name: "Angular", icon: "simple-icons:angular" },
      { name: "Redux", icon: "simple-icons:redux" },
    ],
  },
  {
    key: "ui",
    items: [
      { name: "Tailwind", icon: "simple-icons:tailwindcss" },
      { name: "Vuetify", icon: "simple-icons:vuetify" },
      { name: "Material UI", icon: "simple-icons:mui" },
      { name: "Chakra UI", icon: "simple-icons:chakraui" },
      { name: "Bootstrap", icon: "simple-icons:bootstrap" },
      { name: "Storybook", icon: "simple-icons:storybook" },
      { name: "Webpack", icon: "simple-icons:webpack" },
    ],
  },
  {
    key: "mobile",
    items: [
      { name: "React Native", icon: "simple-icons:react" },
      { name: "Ionic", icon: "simple-icons:ionic" },
      { name: "Capacitor", icon: "simple-icons:capacitor" },
      { name: "NativeScript", icon: "simple-icons:nativescript" },
      { name: "Electron", icon: "simple-icons:electron" },
    ],
  },
  {
    key: "backend",
    items: [
      { name: "Node.js", icon: "simple-icons:nodedotjs" },
      { name: "Express", icon: "simple-icons:express" },
      { name: "NestJS", icon: "simple-icons:nestjs" },
      { name: "Laravel", icon: "simple-icons:laravel" },
      { name: "Symfony", icon: "simple-icons:symfony" },
      { name: "CakePHP", icon: "simple-icons:cakephp" },
      { name: "GraphQL", icon: "simple-icons:graphql" },
      { name: "Apollo", icon: "simple-icons:apollographql" },
      { name: "Socket.io", icon: "simple-icons:socketdotio" },
    ],
  },
  {
    key: "data",
    items: [
      { name: "PostgreSQL", icon: "simple-icons:postgresql" },
      { name: "MySQL", icon: "simple-icons:mysql" },
      { name: "MariaDB", icon: "simple-icons:mariadb" },
      { name: "MongoDB", icon: "simple-icons:mongodb" },
    ],
  },
  {
    key: "devops",
    items: [
      { name: "AWS", icon: "simple-icons:amazonwebservices" },
      { name: "Google Cloud", icon: "simple-icons:googlecloud" },
      { name: "Heroku", icon: "simple-icons:heroku" },
      { name: "Docker", icon: "simple-icons:docker" },
      { name: "Kubernetes", icon: "simple-icons:kubernetes" },
      { name: "NGINX", icon: "simple-icons:nginx" },
      { name: "Linux", icon: "simple-icons:linux" },
      { name: "Jenkins", icon: "simple-icons:jenkins" },
    ],
  },
  {
    key: "testing",
    items: [
      { name: "Playwright", icon: "simple-icons:playwright" },
      { name: "Jest", icon: "simple-icons:jest" },
      { name: "Cypress", icon: "simple-icons:cypress" },
      { name: "Mocha", icon: "simple-icons:mocha" },
      { name: "Postman", icon: "simple-icons:postman" },
    ],
  },
  {
    key: "workflow",
    items: [
      { name: "Git", icon: "simple-icons:git" },
      { name: "Jira", icon: "simple-icons:jira" },
    ],
  },
];
