from epivizfileserver import setup_app, create_fileHandler, MeasurementManager
import os
import numpy
import pickle

if __name__ == "__main__":
    # create measurements manager
    mMgr = MeasurementManager()

    # create file handler
    mHandler = create_fileHandler()

    # genomes are listed in https://obj.umiacs.umd.edu/genomes/index.html
    genome = mMgr.add_genome("hg19")

    fmeasurements = mMgr.import_files(os.getcwd() + "/data.json", mHandler)

    ms = [m for m in fmeasurements if m.annotation["group"] == "H3K9me3"]
    cms = mMgr.add_computed_measurement("computed", "diff_brain_H3K9me3_signal", "Diff Brain H3K9me3 Signal", measurements=ms, 
                    computeFunc=numpy.mean, annotation={"group": "computed_atac"})

    ms = [m for m in fmeasurements if m.annotation["group"] == "H3K27me3"]
    cms = mMgr.add_computed_measurement("computed", "diff_brain_H3K27me3_signal", "Diff Brain H3K27me3 Signal", measurements=ms, 
                    computeFunc=numpy.mean, annotation={"group": "computed_atac"})

    app = setup_app(mMgr)
    app.run(host="0.0.0.0", port=8000)