# Kurum-GPT ile kurumunuzu tanıyan asistan

Bu projemizde GPT Crawler isimli projeyi kullanarak kurumumuzun internet sitesindeki verileri ChatGPT'nin anlayabileceği bir formatta indiriyoruz ve sonra ChatGPT'de bu verilerle konuşabiliyoruz.

Gerekli programı indirmek için aşağıdaki komutu çalıştırınız.

```sh
git clone https://github.com/builderio/gpt-crawler
```

Projenin çalışabilmesi için gerekli olan paketleri indirmek için aşağıdaki komutu çalıştırınız.

```sh
cd gpt-crawler
npm install
```

Projenin ayar dosyası olan config.ts dosyasını kendi kurumumuza göre düzenliyoruz.

```typescript
export const config: Config = {
  // STGM'nin internet sitesini seçtik
  url: "https://www.stgm.org.tr/",
  // Tüm sayfaları çekmelesi için gerekli ayarı yapıyoruz.
  match: "https://www.stgm.org.tr/**",
  // Çekilecek sayfa sayısını belirtiyoruz.
  maxPagesToCrawl: 100,
  // Çıktı dosyasının adını belirtiyoruz.
  outputFileName: "output.json",
  // ChatGPT'nin kullanabileceği maksimum token sayısını belirtiyoruz.
  maxTokens: 2_000_000,
  // Resim, video gibi dosyaların çekilmemesi için gerekli ayarı yapıyoruz.
  resourceExclusions: [
    "png",
    "jpg",
    "jpeg",
    "gif",
    "svg",
    "css",
    "js",
    "ico",
    "woff",
    "woff2",
    "ttf",
    "eot",
    "otf",
    "mp4",
    "mp3",
    "webm",
    "ogg",
    "wav",
    "flac",
    "aac",
    "zip",
    "tar",
    "gz",
    "rar",
    "7z",
    "exe",
    "dmg",
    "apk",
    "csv",
    "xls",
    "xlsx",
    "doc",
    "docx",
    "pdf",
    "epub",
    "iso",
    "dmg",
    "bin",
    "ppt",
    "pptx",
    "odt",
    "avi",
    "mkv",
    "xml",
    "json",
    "yml",
    "yaml",
    "rss",
    "atom",
    "swf",
    "txt",
    "dart",
    "webp",
    "bmp",
    "tif",
    "psd",
    "ai",
    "indd",
    "eps",
    "ps",
    "zipx",
    "srt",
    "wasm",
    "m4v",
    "m4a",
    "webp",
    "weba",
    "m4b",
    "opus",
    "ogv",
    "ogm",
    "oga",
    "spx",
    "ogx",
    "flv",
    "3gp",
    "3g2",
    "jxr",
    "wdp",
    "jng",
    "hief",
    "avif",
    "apng",
    "avifs",
    "heif",
    "heic",
    "cur",
    "ico",
    "ani",
    "jp2",
    "jpm",
    "jpx",
    "mj2",
    "wmv",
    "wma",
    "aac",
    "tif",
    "tiff",
    "mpg",
    "mpeg",
    "mov",
    "avi",
    "wmv",
    "flv",
    "swf",
    "mkv",
    "m4v",
    "m4p",
    "m4b",
    "m4r",
    "m4a",
    "mp3",
    "wav",
    "wma",
    "ogg",
    "oga",
    "webm",
    "3gp",
    "3g2",
    "flac",
    "spx",
    "amr",
    "mid",
    "midi",
    "mka",
    "dts",
    "ac3",
    "eac3",
    "weba",
    "m3u",
    "m3u8",
    "ts",
    "wpl",
    "pls",
    "vob",
    "ifo",
    "bup",
    "svcd",
    "drc",
    "dsm",
    "dsv",
    "dsa",
    "dss",
    "vivo",
    "ivf",
    "dvd",
    "fli",
    "flc",
    "flic",
    "flic",
    "mng",
    "asf",
    "m2v",
    "asx",
    "ram",
    "ra",
    "rm",
    "rpm",
    "roq",
    "smi",
    "smil",
    "wmf",
    "wmz",
    "wmd",
    "wvx",
    "wmx",
    "movie",
    "wri",
    "ins",
    "isp",
    "acsm",
    "djvu",
    "fb2",
    "xps",
    "oxps",
    "ps",
    "eps",
    "ai",
    "prn",
    "svg",
    "dwg",
    "dxf",
    "ttf",
    "fnt",
    "fon",
    "otf",
    "cab",
  ],
};
```

Projenin çalışabilmesi için gerekli olan ayarları yaptıktan sonra aşağıdaki komutu kullanarak çalıştırabiliriz.

```sh
npm start
```

İşlem tamamlandığında gpt-crawler klasörü altında output.json dosyasını göreceksiniz. Bu dosya ChatGPT'de kullanabiliriz ancak kullanmadan önce dosyaların içerisinde tekrar eden ve içeriğe katkı sunmayan kısımları temizlememiz gerekiyor. Dosyayı açıp örneğin aşağıdaki kısmı Cmd + F ile ara ve değiştir özelliğini kullanarak boşluk karakteriyle değiştiriyorum.

```txt
E-Posta Listemize Katılın!\n\nDuyuruların, haberlerin ve etkinliklerin e-posta adresinize gönderilmesini istiyorsanız, e-bülten üyeliğinizi onaylayabilirsiniz.\n\nSTGM Derneği KVKK Aydınlatma Metnini ve Rıza Beyanını okudum, onaylıyorum.\nKişisel verileriniz, Aydınlatma Metni kapsamında işlenmektedir. Formu doldurarak Aydınlatma Metni'ni, Rıza Metni'ni, Gizlilik ve Çerez Politikası'nı okuduğunuzu ve kabul ettiğinizi onaylıyorsunuz.\nSTGM HAKKINDA\nSTGM DESTEKLERİ\nYAYINLAR\nKVKK AYDINLATMA METNİ\nÇEREZ POLİTİKASI\nİLETİŞİM\n     \n\nBu web sitesi Avrupa Birliği'nin maddi desteği ile oluşturulmuştur ve sürdürülmektedir. İçerik tamamıyla Sivil Toplum Geliştirme Merkezi Derneği'nin sorumluluğu altındadır ve Avrupa Birliği'nin görüşlerini yansıtmak zorunda değildir.\n\nBu sitede kullanıcı deneyimini anlamak ve geliştirmek için çerezleri kullanıyoruz.\n\nOnaya veya sitede herhangi bir yere tıklarsanız, STGM Çerez Politikası'nı kabul etmiş sayılacaksınız.\n\nOnay
```

```txt
Ana içeriğe atla\nImage\nEN\nImage\nAnasayfa\n
```

Bu işlemi yaptıktan sonra output.json isimli dosyayı ChatGPT'nin CustomGPT oluşturma sayfasına dosya olarak ekleyiniz.

Dosyanızı ekledikten sonra CustomGPT'nize sorularınızı sorabilirsiniz!
