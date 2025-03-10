export const Info = () => {
  return (
    <div className="info">
      <div className="info-paragraph">
        This app is for encrypting images. On the encryption tab, upload an
        image. Once the image is encrypted, a link will appear for the encrypted
        image, as well as a key. Download the encrypted image. On the Decryption
        tab, upload the encrypted image, paste the key, and submit. A link for
        the decrypted image will appear once decryption is complete.
      </div>
      <div className="info-paragraph">
        This app works best on small images. Large images will be rejected by
        the server. Color images will be converted to black and white.
      </div>
    </div>
  );
};
