# Finance Tracker

Yerel ağda çalışan kişisel finans takip uygulaması. Varlıkları, gelir ve giderleri,
birikim hedeflerini tek bir panelden takip etmeyi amaçlar.

Proje planlama aşamasındadır; henüz çalıştırılabilir bir uygulama bulunmamaktadır.

## Planlanan teknoloji

- Python ve Streamlit
- SQLite
- Pandas ve Plotly
- İsteğe bağlı Gemini ve Telegram entegrasyonları

Kapsam, hedefler ve geliştirme aşamaları için [proje dokümanına](docs/CHARTER.md) bakın.

## GitHub kurulumu

Git ve GitHub CLI (`gh`) kurulu, GitHub oturumu açık olmalıdır.
GitHub üzerinde boş, public bir `finance-tracker` reposu oluşturduktan sonra
proje klasöründe aşağıdaki komut yerel projeyi repoya bağlar, ilk commit'i
gönderir ve temel repo ayarlarını uygular:

```bash
bash scripts/setup-github.sh
```

Varsayılan olarak açık GitHub hesabının `finance-tracker` reposu kullanılır.
Başka bir repo için bağlantısını veya `kullanici/repo` adını verebilirsiniz:

```bash
bash scripts/setup-github.sh https://github.com/KULLANICI/finance-tracker
```

Varsayılan dal `main` olur. Issues ve squash merge açılır; birleşen dallar
otomatik silinir. Secret scanning ve push protection etkinleştirilir.

## Yerel veriler

API anahtarları, `.env` dosyaları, SQLite veritabanları, dışa aktarımlar ve
yedekler Git dışında tutulur. Örnek yapılandırma gerekiyorsa gerçek anahtarlar
içermeyen `.env.example` kullanın.
