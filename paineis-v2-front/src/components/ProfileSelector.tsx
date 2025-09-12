import usePortal from '../hooks/usePortal';

const ProfileSelector = () => {
  const Portal: any = usePortal(document.querySelector('body'));

  return (
    <Portal>
      <div
        style={{
          position: 'absolute',
          width: '100vw',
          height: '100vh',
          backgroundColor: 'white',
          zIndex: 9999,
        }}
      >
        ok
      </div>
    </Portal>
  );
};

export default ProfileSelector;
