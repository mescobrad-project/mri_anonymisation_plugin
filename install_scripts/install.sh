#!/bin/bash

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd )

BASEPATH=$(dirname "$ROOT_DIR")

wget -O $BASEPATH/deface_files/mri_deface \
 ftp://surfer.nmr.mgh.harvard.edu/pub/dist/mri_deface/mri_deface_linux && \
 chmod +x $BASEPATH/deface_files/mri_deface

wget -O $BASEPATH/deface_files/face.gca.gz \
 ftp://surfer.nmr.mgh.harvard.edu/pub/dist/mri_deface/face.gca.gz && \
 gunzip $BASEPATH/deface_files/face.gca.gz

wget -O $BASEPATH/deface_files/talairach_mixed_with_skull.gca.gz \
 ftp://surfer.nmr.mgh.harvard.edu/pub/dist/mri_deface/talairach_mixed_with_skull.gca.gz && \
 gunzip $BASEPATH/deface_files/talairach_mixed_with_skull.gca.gz
