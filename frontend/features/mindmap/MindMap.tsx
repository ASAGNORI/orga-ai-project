import React from 'react';
import dynamic from 'next/dynamic';

const MindMap = () => {
  React.useEffect(() => {
    const loadMindElixir = async () => {
      const MindElixir = (await import('mind-elixir')).default;
      const mind = new MindElixir({
        el: '#map',
        direction: 2, // LEFT
        data: {
          nodeData: {
            id: 'root',
            topic: 'Orga AI',
            children: []
          }
        },
        draggable: true,
        contextMenu: true,
      });
      mind.init();
    };

    loadMindElixir();
  }, []);

  return <div id="map" style={{ width: '100%', height: '600px', backgroundColor: '#f0f0f0' }} />;
};

export default MindMap;