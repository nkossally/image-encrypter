import classNames from "classnames"
export const Info = () => {
  return (
    <div className={classNames("info", "fade-in")}>
      <div className="info-paragraph">
        This app is for encrypting images using the Advanced Encryption Standard
        (AES). On the encryption tab, upload an image. Once the image is
        encrypted, a link will appear for the encrypted image, as well as a key.
        This may take up to a minute. Download the encrypted image. On the
        Decryption tab, upload the encrypted image, paste the key, and submit. A
        link for the decrypted image will appear once decryption is complete.
      </div>
      <div className="info-paragraph">
        If an image is too large to be encrypted/decrypted by the server, try a
        smaller image. Color images will be converted to black and white.
      </div>
    </div>
  );
};
