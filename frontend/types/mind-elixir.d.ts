declare module 'mind-elixir' {
  interface MindElixirData {
    nodeData: {
      id: string;
      topic: string;
      children: any[];
    };
  }

  interface MindElixirOptions {
    el: string;
    direction: number;
    data: MindElixirData;
    draggable: boolean;
    contextMenu: boolean;
  }

  class MindElixir {
    constructor(options: MindElixirOptions);
    init(): void;
  }

  export default MindElixir;
} 