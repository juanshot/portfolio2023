export const useCal = () => {
  const isOpen = useState<boolean>("isCalOpen", () => false);

  return {
    isOpen,
    open: () => {
      isOpen.value = true;
    },
    close: () => {
      isOpen.value = false;
    },
  };
};
