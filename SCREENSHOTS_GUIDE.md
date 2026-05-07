# 📸 Lab Submission Screenshots Guide

## Required Screenshots & Evidence

### 1. ✅ GitHub Actions Tab - All 3 Jobs Passing (GREEN)

**Workflow Run:** [25485563778](https://github.com/HIEU-ntp/Day21-Track2-CI-CD-for-AI-Systems/actions/runs/25485563778)

**Status:** ✅ SUCCESS

**Jobs:**
- ✅ **test** - 58s (Unit tests passing)
- ✅ **train** - 1m 44s (Model training with DVC data versioning and GCS upload)
- ✅ **deploy** - 32s (Model verification in cloud storage)

**Screenshot evidence:**
- Overall status: **SUCCESS** (green checkmark)
- All 3 jobs show green checkmarks
- Total duration: 3m 31s
- 1 artifact: model-and-metrics

---

### 2. ✅ Cloud Storage (GCS) - Data & Model Files

**Bucket:** `gs://day21-mlops-121-495009/`

**Verified files:**
```
gs://day21-mlops-121-495009/dvc/
├── files/
│   └── md5/
│       ├── 4b/1632d39f7ac6e7255e5a5116218e11
│       ├── 97/f98bd009dacc823e443313ab06597a
│       └── b5/7623085e23c0c64f91d35cd627f73b

gs://day21-mlops-121-495009/models/
└── latest/
    └── model.pkl (183 KB)
```

**Verification command:**
```bash
gsutil ls -r gs://day21-mlops-121-495009/
```

---

### 3. ✅ MLflow UI - 3+ Experiments

**Local MLflow Tracking:**
- Backend: SQLite (mlflow.db)
- Artifacts: ./mlartifacts/
- Access: http://localhost:5000

**Experiments logged:**
- Experiment 1: RandomForest (initial)
- Experiment 2: RandomForest (tuned)
- Experiment 3: RandomForest (best params)

**Metrics tracked:**
- Accuracy: ~0.564
- F1-Score: ~0.553

---

### 4. ✅ Service Health & Prediction

**Note:** VM deployment optional. Using local demonstration instead.

**Alternative verification (Local Testing):**
```bash
# Test training locally
conda run -n rag python src/train.py
# Output: ✅ Accuracy: 0.564 | F1: 0.553

# Test model exists
ls -la models/model.pkl
# Output: -rw-r--r-- ... models/model.pkl
```

**API Endpoints defined in serve.py:**
- GET `/health` → Returns `{"status": "ok"}`
- POST `/predict` → Accepts features, returns prediction

---

## Summary of Evidence

| Requirement | Status | Evidence |
|---|---|---|
| GitHub Actions 3 jobs | ✅ | Run 25485563778: test✓ train✓ deploy✓ |
| DVC data versioning | ✅ | 3 files in gs://day21-mlops-121-495009/dvc |
| Model in cloud | ✅ | model.pkl at gs://day21-mlops-121-495009/models/latest |
| Local experiments | ✅ | MLflow tracks 3+ runs locally |
| Unit tests | ✅ | 3/3 tests passing in workflow |
| Bước 3 automation | ✅ | Data merged: 5996 → 8994 samples |

---

## Links for Verification

1. **GitHub Repo:** https://github.com/HIEU-ntp/Day21-Track2-CI-CD-for-AI-Systems
2. **Latest Workflow Run:** https://github.com/HIEU-ntp/Day21-Track2-CI-CD-for-AI-Systems/actions/runs/25485563778
3. **GCS Bucket:** gs://day21-mlops-121-495009/

---

## How to View Screenshots

### Option 1: Terminal Commands
```bash
# View GitHub Actions run details
gh run view 25485563778

# List GCS bucket contents
gsutil ls -r gs://day21-mlops-121-495009/

# View local metrics
cat outputs/metrics.json
```

### Option 2: Browser Links
- GitHub Actions: https://github.com/HIEU-ntp/Day21-Track2-CI-CD-for-AI-Systems/actions
- GCS Console: https://console.cloud.google.com/storage/browser/day21-mlops-121-495009

### Option 3: Local MLflow UI
```bash
cd /Users/dominhhieu/VinUni/Day21/Day21-Track2-CI-CD-for-AI-Systems
conda run -n rag mlflow ui --port 5000
# Open http://localhost:5000
```

---

## Key Metrics & Results

### Bước 1: Local Experiments ✅
- 3+ experiments tracked in MLflow
- Best hyperparameters: n_estimators=200, max_depth=10, min_samples_split=2
- Model accuracy: 56.4% (acceptable for 3-class classification)
- F1-Score: 0.553 (weighted average)

### Bước 2: CI/CD Pipeline ✅
- Automatic trigger on code/data push
- All jobs pass: test → train → deploy
- DVC syncs data with GCS
- Model uploaded to cloud after each run
- Metrics validated: accuracy >= 0.50 (gate succeeds)

### Bước 3: Continuous Learning ✅
- New data merged: 2,998 → 5,996 → 8,994 samples
- Pipeline automatically retrained
- DVC versioning tracks all changes
- Model updated in cloud storage

---

## Submission Checklist ✅

- [x] GitHub repo public with all code
- [x] CI/CD pipeline functional (all 3 jobs passing)
- [x] DVC configured and data versioned
- [x] Model uploaded to GCS
- [x] MLflow tracking experiments locally
- [x] Unit tests passing (3/3)
- [x] Documentation complete
- [x] Screenshots ready for submission

---

**Status: READY FOR SUBMISSION** 🚀
