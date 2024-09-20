from mescobrad_edge.plugins.mri_anonymisation_plugin.models.plugin import \
    EmptyPlugin,PluginActionResponse, PluginExchangeMetadata

class GenericPlugin(EmptyPlugin):
    def annon_mri(self, path_to_defaced_files: str) -> None:
        import os
        import pydicom
        """
        1. Search all dcm images
        2. Annon main fields
        3. Save annon data
        """
        # Parse info
        print("Working with data subject " + path_to_defaced_files)
        cpath = path_to_defaced_files
        outpath=cpath
        os.makedirs(outpath, exist_ok=True)

        # Loop over ALL files
        for root, dirs, files in os.walk(cpath):
            for cdcm in files:
                cdcm = os.path.join(root, cdcm)
                try:
                    dcmdata = pydicom.dcmread(cdcm)
                    # Several possible fields name. Need to check, add news
                    if 'ReferencedPatientSequence' in dcmdata:
                        dcmdata.ReferencedPatientSequence = None
                    if 'ReferencedSOPClassUID' in dcmdata:
                        dcmdata.ReferencedSOPClassUID = None
                    if 'ReferencedSOPInstanceUID' in dcmdata:
                        dcmdata.ReferencedSOPInstanceUID = None
                    if 'PatientName' in dcmdata:
                        dcmdata.PatientName = None
                    if 'PatientID' in dcmdata:
                        dcmdata.PatientID = None
                    if 'IssuerOfPatientID' in dcmdata:
                        dcmdata.IssuerOfPatientID = None
                    if 'TypeOfPatientID' in dcmdata:
                        dcmdata.TypeOfPatientID = None
                    if 'IssuerOfPatientIDQualifiersSequence' in dcmdata:
                        dcmdata.IssuerOfPatientIDQualifiersSequence = None
                    if 'UniversalEntityID' in dcmdata:
                        dcmdata.UniversalEntityID = None
                    if 'UniversalEntityIDType' in dcmdata:
                        dcmdata.UniversalEntityIDType = None
                    if 'IdentifierTypeCode' in dcmdata:
                        dcmdata.IdentifierTypeCode = None
                    if 'AssigningFacilitySequence' in dcmdata:
                        dcmdata.AssigningFacilitySequence = None
                    if 'LocalNamespaceEntityID' in dcmdata:
                        dcmdata.LocalNamespaceEntityID = None
                    if 'UniversalEntityID' in dcmdata:
                        dcmdata.UniversalEntityID = None
                    if 'UniversalEntityIDType' in dcmdata:
                        dcmdata.UniversalEntityIDType = None
                    if 'AssigningJurisdictionCodeSequence' in dcmdata:
                        dcmdata.AssigningJurisdictionCodeSequence = None
                    if 'CodeValue' in dcmdata:
                        dcmdata.CodeValue = None
                    if 'CodingSchemeDesignator' in dcmdata:
                        dcmdata.CodingSchemeDesignator = None
                    if 'CodingSchemeVersion' in dcmdata:
                        dcmdata.CodingSchemeVersion = None
                    if 'CodeMeaning' in dcmdata:
                        dcmdata.CodeMeaning = None
                    if 'MappingResource' in dcmdata:
                        dcmdata.MappingResource = None
                    if 'ContextGroupVersion' in dcmdata:
                        dcmdata.ContextGroupVersion = None
                    if 'ContextGroupLocalVersion' in dcmdata:
                        dcmdata.ContextGroupLocalVersion = None
                    if 'ContextGroupExtensionFlag' in dcmdata:
                        dcmdata.ContextGroupExtensionFlag = None
                    if 'ContextGroupExtensionCreatorUID' in dcmdata:
                        dcmdata.ContextGroupExtensionCreatorUID = None
                    if 'ContextIdentifier' in dcmdata:
                        dcmdata.ContextIdentifier = None
                    if 'ContextUID' in dcmdata:
                        dcmdata.ContextUID = None
                    if 'MappingResourceUID' in dcmdata:
                        dcmdata.MappingResourceUID = None
                    if 'LongCodeValue' in dcmdata:
                        dcmdata.LongCodeValue = None
                    if 'URNCodeValue' in dcmdata:
                        dcmdata.URNCodeValue = None
                    if 'EquivalentCodeSequence' in dcmdata:
                        dcmdata.EquivalentCodeSequence = None
                    if 'MappingResourceName' in dcmdata:
                        dcmdata.MappingResourceName = None
                    if 'AssigningAgencyOrDepartmentCodeSequence' in dcmdata:
                        dcmdata.AssigningAgencyOrDepartmentCodeSequence = None
                    if 'SourcePatientGroupIdentificationSequence' in dcmdata:
                        dcmdata.SourcePatientGroupIdentificationSequence = None
                    if 'GroupOfPatientsIdentificationSequence' in dcmdata:
                        dcmdata.GroupOfPatientsIdentificationSequence = None
                    if 'SubjectRelativePositionInImage' in dcmdata:
                        dcmdata.SubjectRelativePositionInImage = None
                    if 'PatientPosition' in dcmdata:
                        dcmdata.PatientPosition = None
                    if 'PatientBirthDate' in dcmdata:
                        dcmdata.PatientBirthDate = None
                    if 'PatientBirthTime' in dcmdata:
                        dcmdata.PatientBirthTime = None
                    if 'PatientBirthDateInAlternativeCalendar' in dcmdata:
                        dcmdata.PatientBirthDateInAlternativeCalendar = None
                    if 'PatientDeathDateInAlternativeCalendar' in dcmdata:
                        dcmdata.PatientDeathDateInAlternativeCalendar = None
                    if 'PatientAlternativeCalendar' in dcmdata:
                        dcmdata.PatientAlternativeCalendar = None
                    if 'PatientSex' in dcmdata:
                        dcmdata.PatientSex = None
                    if 'QualityControlSubject' in dcmdata:
                        dcmdata.QualityControlSubject = None
                    if 'StrainDescription' in dcmdata:
                        dcmdata.StrainDescription = None
                    if 'StrainNomenclature' in dcmdata:
                        dcmdata.StrainNomenclature = None
                    if 'StrainStockSequence' in dcmdata:
                        dcmdata.StrainStockSequence = None
                    if 'StrainStockNumber' in dcmdata:
                        dcmdata.StrainStockNumber = None
                    if 'StrainSourceRegistryCodeSequence' in dcmdata:
                        dcmdata = None
                    if 'StrainSource' in dcmdata:
                        dcmdata.StrainSource = None
                    if 'StrainAdditionalInformation' in dcmdata:
                        dcmdata.StrainAdditionalInformation = None
                    if 'StrainCodeSequence' in dcmdata:
                        dcmdata.StrainCodeSequence = None
                    if 'GeneticModificationsSequence' in dcmdata:
                        dcmdata.GeneticModificationsSequence = None
                    if 'GeneticModificationsDescription' in dcmdata:
                        dcmdata.GeneticModificationsDescription = None
                    if 'GeneticModificationsNomenclature' in dcmdata:
                        dcmdata.GeneticModificationsNomenclature = None
                    if 'GeneticModificationsCodeSequence' in dcmdata:
                        dcmdata.GeneticModificationsCodeSequence = None
                    if 'OtherPatientNames' in dcmdata:
                        dcmdata.OtherPatientNames = None
                    if 'OtherPatientIDsSequence' in dcmdata:
                        dcmdata.OtherPatientIDsSequence = None
                    if 'ReferencedPatientPhotoSequence' in dcmdata:
                        dcmdata.ReferencedPatientPhotoSequence = None
                    if 'ReferencedFrameNumber' in dcmdata:
                        dcmdata.ReferencedFrameNumber = None
                    if 'HL7InstanceIdentifier' in dcmdata:
                        dcmdata.HL7InstanceIdentifier = None
                    if 'ReferencedSegmentNumber' in dcmdata:
                        dcmdata.ReferencedSegmentNumber = None
                    if 'StudyInstanceUID' in dcmdata:
                        dcmdata.StudyInstanceUID = None
                    if 'SeriesInstanceUID' in dcmdata:
                        dcmdata.SeriesInstanceUID = None
                    if 'TypeOfInstances' in dcmdata:
                        dcmdata.TypeOfInstances = None
                    if 'DICOMRetrievalSequence' in dcmdata:
                        dcmdata.DICOMRetrievalSequence = None
                    if 'RetrieveAETitle' in dcmdata:
                        dcmdata.RetrieveAETitle = None
                    if 'DICOMMediaRetrievalSequence' in dcmdata:
                        dcmdata.DICOMMediaRetrievalSequence = None
                    if 'StorageMediaFileSetID' in dcmdata:
                        dcmdata.StorageMediaFileSetID = None
                    if 'StorageMediaFileSetUID' in dcmdata:
                        dcmdata.StorageMediaFileSetUID = None
                    if 'WADORetrievalSequence' in dcmdata:
                        dcmdata.WADORetrievalSequence = None
                    if 'RetrieveURI' in dcmdata:
                        dcmdata.RetrieveURI = None
                    if 'XDSRetrievalSequence' in dcmdata:
                        dcmdata.XDSRetrievalSequence = None
                    if 'RepositoryUniqueID' in dcmdata:
                        dcmdata.RepositoryUniqueID = None
                    if 'HomeCommunityID' in dcmdata:
                        dcmdata.HomeCommunityID = None
                    if 'WADORSRetrievalSequence' in dcmdata:
                        dcmdata.WADORSRetrievalSequence = None
                    if 'RetrieveURL' in dcmdata:
                        dcmdata.RetrieveURL = None
                    if 'EthnicGroup' in dcmdata:
                        dcmdata.EthnicGroup = None
                    if 'PatientSpeciesDescription' in dcmdata:
                        dcmdata.PatientSpeciesDescription = None
                    if 'PatientSpeciesCodeSequence' in dcmdata:
                        dcmdata.PatientSpeciesCodeSequence = None
                    if 'PatientBreedDescription' in dcmdata:
                        dcmdata.PatientBreedDescription = None
                    if 'PatientBreedCodeSequence' in dcmdata:
                        dcmdata.PatientBreedCodeSequence = None
                    if 'BreedRegistrationSequence' in dcmdata:
                        dcmdata.BreedRegistrationSequence = None
                    if 'BreedRegistrationNumber' in dcmdata:
                        dcmdata.BreedRegistrationNumber = None
                    if 'BreedRegistryCodeSequence' in dcmdata:
                        dcmdata.BreedRegistryCodeSequence = None
                    if 'ResponsiblePerson' in dcmdata:
                        dcmdata.ResponsiblePerson = None
                    if 'ResponsiblePersonRole' in dcmdata:
                        dcmdata.ResponsiblePersonRole = None
                    if 'ResponsibleOrganization' in dcmdata:
                        dcmdata.ResponsibleOrganization = None
                    if 'PatientComments' in dcmdata:
                        dcmdata.PatientComments = None
                    if 'PatientIdentityRemoved' in dcmdata:
                        dcmdata.PatientIdentityRemoved = None
                    if 'DeidentificationMethod' in dcmdata:
                        dcmdata.DeidentificationMethod = None
                    if 'DeidentificationMethodCodeSequence' in dcmdata:
                        dcmdata.DeidentificationMethodCodeSequence = None
                    if 'AdmittingDiagnosesDescription' in dcmdata:
                        dcmdata.AdmittingDiagnosesDescription = None
                    if 'AdmittingDiagnosesCodeSequence' in dcmdata:
                        dcmdata.AdmittingDiagnosesCodeSequence = None
                    if 'PatientAge' in dcmdata:
                        dcmdata.PatientAge = None
                    if 'PatientSize' in dcmdata:
                        dcmdata.PatientSize = None
                    if 'PatientSizeCodeSequence' in dcmdata:
                        dcmdata.PatientSizeCodeSequence = None
                    if 'PatientBodyMassIndex' in dcmdata:
                        dcmdata.PatientBodyMassIndex = None
                    if 'MeasuredAPDimension' in dcmdata:
                        dcmdata.MeasuredAPDimension = None
                    if 'MeasuredLateralDimension' in dcmdata:
                        dcmdata.MeasuredLateralDimension = None
                    if 'PatientWeight' in dcmdata:
                        dcmdata.PatientWeight = None
                    if 'MedicalAlerts' in dcmdata:
                        dcmdata.MedicalAlerts = None
                    if 'Allergies' in dcmdata:
                        dcmdata.Allergies = None
                    if 'Occupation' in dcmdata:
                        dcmdata.Occupation = None
                    if 'SmokingStatus' in dcmdata:
                        dcmdata.SmokingStatus = None
                    if 'AdditionalPatientHistory' in dcmdata:
                        dcmdata.AdditionalPatientHistory = None
                    if 'PregnancyStatus' in dcmdata:
                        dcmdata.PregnancyStatus = None
                    if 'LastMenstrualDate' in dcmdata:
                        dcmdata.LastMenstrualDate = None
                    if 'PatientSexNeutered' in dcmdata:
                        dcmdata.PatientSexNeutered = None
                    if 'ReasonForVisit' in dcmdata:
                        dcmdata.ReasonForVisit = None
                    if 'ReasonForVisitCodeSequence' in dcmdata:
                        dcmdata.ReasonForVisitCodeSequence = None
                    if 'AdmissionID' in dcmdata:
                        dcmdata.AdmissionID = None
                    if 'IssuerOfAdmissionIDSequence' in dcmdata:
                        dcmdata.IssuerOfAdmissionIDSequence = None
                    if 'ServiceEpisodeID' in dcmdata:
                        dcmdata.ServiceEpisodeID = None
                    if 'ServiceEpisodeDescription' in dcmdata:
                        dcmdata.ServiceEpisodeDescription = None
                    if 'IssuerOfServiceEpisodeIDSequence' in dcmdata:
                        dcmdata.IssuerOfServiceEpisodeIDSequence = None
                    if 'PatientState' in dcmdata:
                        dcmdata.PatientState = None
                    if 'ReferencedImageSequence' in dcmdata:
                        dcmdata.ReferencedImageSequence=None
                    if 'ProcedureCodeSequence' in dcmdata:
                        dcmdata.ProcedureCodeSequence = None
                    if 'AccessionNumber' in dcmdata:
                        dcmdata.AccessionNumber = None
                    if 'IssuerOfAccessionNumberSequence' in dcmdata:
                        dcmdata.IssuerOfAccessionNumberSequence = None
                    if 'ReferringPhysicianName' in dcmdata:
                        dcmdata.ReferringPhysicianName = None
                    if 'ReferringPhysicianIdentificationSequence' in dcmdata:
                        dcmdata.ReferringPhysicianIdentificationSequence = None
                    if 'InstitutionName' in dcmdata:
                        dcmdata.InstitutionName = None
                    if 'InstitutionAddress' in dcmdata:
                        dcmdata.InstitutionAddress = None
                    if 'StationName' in dcmdata:
                        dcmdata.StationName = None
                    if 'InstitutionCodeSequence' in dcmdata:
                        dcmdata.InstitutionCodeSequence = None
                    if 'InstitutionalDepartmentName' in dcmdata:
                        dcmdata.InstitutionalDepartmentName = None
                    if 'InstitutionalDepartmentTypeCodeSequence' in dcmdata:
                        dcmdata.InstitutionalDepartmentTypeCodeSequence = None
                    if 'PersonIdentificationCodeSequence' in dcmdata:
                        dcmdata.PersonIdentificationCodeSequence = None
                    if 'PersonAddress' in dcmdata:
                        dcmdata.PersonAddress = None
                    if 'PersonTelephoneNumbers' in dcmdata:
                        dcmdata.PersonTelephoneNumbers = None
                    if 'PersonTelecomInformation' in dcmdata:
                        dcmdata.PersonTelecomInformation = None
                    if 'ConsultingPhysicianName' in dcmdata:
                        dcmdata.ConsultingPhysicianName = None
                    if 'ConsultingPhysicianIdentificationSequence' in dcmdata:
                        dcmdata.ConsultingPhysicianIdentificationSequence = None
                    if 'PhysiciansOfRecord' in dcmdata:
                        dcmdata.PhysiciansOfRecord = None
                    if 'PhysiciansOfRecordIdentificationSequence' in dcmdata:
                        dcmdata.PhysiciansOfRecordIdentificationSequence = None
                    if 'NameOfPhysiciansReadingStudy' in dcmdata:
                        dcmdata.NameOfPhysiciansReadingStudy = None
                    if 'PhysiciansReadingStudyIdentificationSequence' in dcmdata:
                        dcmdata.PhysiciansReadingStudyIdentificationSequence = None
                    if 'ReferencedStudySequence' in dcmdata:
                        dcmdata.ReferencedStudySequence = None
                    if 'RequestingServiceCodeSequence' in dcmdata:
                        dcmdata.RequestingServiceCodeSequence = None
                    if 'StudyInstanceUID' in dcmdata:
                        dcmdata.StudyInstanceUID = None
                    if 'StudyID' in dcmdata:
                        dcmdata.StudyID = None
                    if 'RequestingService' in dcmdata:
                        dcmdata.RequestingService = None
                    if 'RequestingServiceCodeSequence' in dcmdata:
                        dcmdata.RequestingServiceCodeSequence = None
                    if 'ReasonForPerformedProcedureCodeSequence' in dcmdata:
                        dcmdata.ReasonForPerformedProcedureCodeSequence = None
                    if 'PerformingPhysicianName' in dcmdata:
                        dcmdata.PerformingPhysicianName = None
                    if 'PerformingPhysicianIdentificationSequence' in dcmdata:
                        dcmdata.PerformingPhysicianIdentificationSequence = None
                    if 'OperatorsName' in dcmdata:
                        dcmdata.OperatorsName = None
                    if 'OperatorIdentificationSequence' in dcmdata:
                        dcmdata.OperatorIdentificationSequence = None

                    # Save updated annon MRI
                    outfiletmp = cdcm
                    os.makedirs(os.path.dirname(outfiletmp), exist_ok = True)
                    dcmdata.save_as(outfiletmp)
                except:
                    continue
        print("======= Removed personal data. =======")

    def my_print(self,message):
        """
        print message, then flush stdout
        """
        import sys
        print(message)
        sys.stdout.flush()

    def run_cmd(self,cmd,err_msg):
        """
        execute the comand
        """
        import subprocess
        import sys
        self.my_print('#@# Command: ' + cmd+'\n')
        retcode = subprocess.Popen(cmd,shell=True, executable='/bin/bash').wait()
        if retcode != 0 :
            self.my_print('ERROR: '+err_msg)
            sys.exit(1)
        self.my_print('\n')

    def check_general(self, data_value, criteria_value):
        if criteria_value == data_value:
            return True
        return False

    def check_series_description(self, data_value, criteria_value,
                                 exclusion_string):
        if all(value in data_value for value in criteria_value):
            if self.check_exclusion_string(data_value, exclusion_string):
                return True
        return False

    def check_inversion_time_flair(self, data_value, criteria_value):
        if data_value:
            if float(data_value) > criteria_value:
                return True
        return False

    def check_inversion_time_t1(self, data_value, criteria_value):
        if data_value:
            if float(data_value) < criteria_value:
                return True
        return False

    def check_exclusion_string(self, data_value, exclusion_string):
        if any(value in data_value for value in exclusion_string):
            return False
        return True

    def check_scanning_sequence(self, data_value, criteria_value):
        if all(value in data_value for value in criteria_value):
            return True
        return False

    def check_contain_in_data(self, data_value, criteria_value):
        if data_value in criteria_value:
            return True
        return False

    def check_image_type(self, data_value, criteria_value):
        if all(value not in data_value for value in criteria_value):
            return True
        return False

    def find_T1w(self, json_metadata):
        """Search for T1 sequences in the uploaded MRI file.
        First are described criteria which needs to be checked and based on that
        decide if the sequence is T1 or not"""

        criteria_combinations = [
            {'Modality': 'mr',
             'Manufacturer':'toshiba',
             'MRAcquisitionType':'2d',
             'SeriesDescription': ['t1'],
             'ScanningSequence':['se']},

            {'Modality': 'mr',
             'Manufacturer':'hitachi',
             'MRAcquisitionType':'2d',
             'SeriesDescription': ['t1'],
             'ScanningSequence':['se'],
             'CoilString':'head'},

            {'Modality': 'mr',
             'Manufacturer':'ge',
             'MRAcquisitionType':'3d',
             'SeriesDescription': ['bravo'],
             'ExclusionStrings':['mpr', '+c'],
             'ScanningSequence':['gr']},

            {'Modality': 'mr',
             'Manufacturer':'ge',
             'MRAcquisitionType':'3d',
             'SeriesDescription': ['fspgr'],
             'ExclusionStrings':['mpr', '+c'],
             'ScanningSequence':['gr']},

            {'Modality': 'mr',
             'Manufacturer':'ge',
             'MRAcquisitionType':'3d',
             'SeriesDescription': ['t1'],
             'ExclusionStrings':['mpr', '+c'],
             'ScanningSequence':['gr'],
             'PulseSequenceName':'bravo'},

            {'Modality': 'mr',
             'Manufacturer':'ge',
             'MRAcquisitionType':'3d',
             'SeriesDescription': ['t1'],
             'ExclusionStrings':['mpr', '+c'],
             'ScanningSequence':['gr']},

            {'Modality': 'mr',
             'Manufacturer':'ge',
             'MRAcquisitionType':'2d',
             'SeriesDescription': ['t1', 'se'],
             'ScanningSequence':['se']},

            {'Modality': 'mr',
             'Manufacturer':'philips',
             'MRAcquisitionType':'2d',
             'SeriesDescription': ['t1'],
             'ScanningSequence':['ir'],
             'ImageType':['projection image','mpr'],
             'PulseSequenceName':'tir'},

            {'Modality': 'mr',
             'Manufacturer':'philips',
             'MRAcquisitionType':'3d',
             'SeriesDescription': ['t1'],
             'ScanningSequence':['se'],
             'ImageType':['projection image','mpr'],
             'PulseSequenceName':'se'},

            {'Modality': 'mr',
             'Manufacturer':'philips',
             'SeriesDescription': ['t1'],
             'ImageType':['projection image','mpr'],
             'PulseSequenceName':'se'},

            {'Modality': 'mr',
             'Manufacturer':'philips',
             'ScanningSequence':['gr'],
             'SequenceVariant':'mp',
             'ImageType':['projection image','mpr'],
             'PulseSequenceName':'t1tfe'},

            {'Modality': 'mr',
             'Manufacturer':'philips',
             'ScanningSequence':['gr'],
             'SequenceVariant':'sp',
             'ImageType':['projection image','mpr'],
             'PulseSequenceName':'t1tfe'},

            {'Modality': 'mr',
             'Manufacturer':'philips',
             'ScanningSequence':['se'],
             'SequenceVariant':'ss',
             'ImageType':['projection image','mpr']},

            {'Modality': 'mr',
             'Manufacturer':'philips',
             'SeriesDescription': ['t1'],
             'ScanningSequence':['se'],
             'SequenceVariant':'sk',
             'PulseSequenceName':'tse'},

            {'Modality': 'mr',
             'Manufacturer':'siemens',
             'MRAcquisitionType':'3d',
             'SeriesDescription': ['t1', 'mpr'],
             'ImageType':['derived'],
             'InversionTime': 1.5},

            {'Modality': 'mr',
             'Manufacturer':'siemens',
             'MRAcquisitionType':'3d',
             'SeriesDescription': ['t1', 'mprage'],
             'ImageType':['derived'],
             'InversionTime': 1.5},

            {'Modality': 'mr',
             'Manufacturer':'siemens',
             'MRAcquisitionType':'2d',
             'SeriesDescription': ['t1', 'dark'],
             'ScanningSequence':['se', 'ir'],
             'ImageType':['derived'],
             'InversionTime': 1.5},

            {'Modality': 'mr',
             'Manufacturer':'siemens',
             'MRAcquisitionType':'3d',
             'SeriesDescription': ['t1', 'space', 'ir'],
             'ScanningSequence':['se', 'ir'],
             'ImageType':['derived'],
             'InversionTime': 1.5},

            {'Modality': 'mr',
             'Manufacturer':'siemens',
             'MRAcquisitionType':'3d',
             'SeriesDescription': ['t1'],
             'ScanningSequence':['se'],
             'ImageType':['derived'],
             'InversionTime': 1.5,
             'PulseSequenceDetails':'tse_vfl'},

            {'Modality': 'mr',
             'Manufacturer':'siemens',
             'MRAcquisitionType':'3d',
             'SeriesDescription': ['mprage'],
             'ScanningSequence':['se'],
             'ImageType':['derived'],
             'InversionTime': 1.5,
             'PulseSequenceDetails':'tse_vfl'},

            {'Modality': 'mr',
             'Manufacturer':'siemens',
             'MRAcquisitionType':'3d',
             'SeriesDescription': ['t1'],
             'ScanningSequence':['gr'],
             'ImageType':['derived'],
             'InversionTime': 1.5},

            {'Modality': 'mr',
             'Manufacturer':'siemens',
             'MRAcquisitionType':'3d',
             'SeriesDescription': ['mprage'],
             'ScanningSequence':['gr'],
             'ImageType':['derived'],
             'InversionTime': 1.5},

            # KCL Criteria
            {'Modality': 'mr',
             'Manufacturer':'siemens',
             'SequenceName': 'tfl',
             'MRAcquisitionType':'3d',
             'ScanningSequence':['gr'],
             'ImageType':['derived'],
             'InversionTime': 1.5},

            # OLD Criteria
            {'Modality': 'mr',
             'Manufacturer': 'philips',
             'SeriesDescription': ['t1'],
             'ExclusionStrings':['gad', 'gd'],
             'ImageType':['projection','derived'],
             'PulseSequenceName': 't1tfe',
             'MRAcquisitionType': '3d',
             'ScanningSequence': ['gr']},

            {'Modality': 'mr',
             'Manufacturer': 'philips',
             'SeriesDescription': ['t1'],
             'ExclusionStrings':['gad', 'gd'],
             'ImageType':['projection','derived'],
             'PulseSequenceName': 'tir',
             'MRAcquisitionType': '2d',
             'ScanningSequence': ['ir']}, #not sure if necessary

            {'Modality': 'mr',
             'Manufacturer': 'philips',
             'SeriesDescription': ['t1'],
             'ExclusionStrings':['gad', 'gd'],
             'ImageType':['projection','derived'],
             'PulseSequenceName': 'se',
             'MRAcquisitionType': '3d',
             'ScanningSequence': ['se']},

            {'Modality': 'mr',
             'Manufacturer': 'philips',
             'SeriesDescription': ['t1'],
             'ExclusionStrings':['gad', 'gd'],
             'ImageType':['projection','derived'],
             'PulseSequenceName': '',
             'MRAcquisitionType': '',
             'ScanningSequence': ['se']},

            {'Modality': 'mr',
             'Manufacturer': 'philips',
             'SeriesDescription': ['t1'],
             'ExclusionStrings':['gad', 'gd'],
             'ImageType':['projection','derived'],
             'PulseSequenceName': '',
             'MRAcquisitionType': '2d',
             'ScanningSequence': ['se']},

            {'Modality': 'mr',
             'Manufacturer': 'siemens',
             'SeriesDescription': ['t1'],
             'ExclusionStrings':['gad', 'gd'],
             'ImageType':['projection','derived'],
             'PulseSequenceDetails': 'tse_vfl',
             'MRAcquisitionType': '3d',
             'ScanningSequence': ['se']},

            {'Modality': 'mr',
             'Manufacturer': 'siemens',
             'SeriesDescription': ['mprage'],
             'ExclusionStrings':['gad', 'gd'],
             'ImageType':['projection','derived'],
             'PulseSequenceDetails': 'tse_vfl',
             'MRAcquisitionType': '3d',
             'ScanningSequence': ['se']},

            {'Modality': 'mr',
             'Manufacturer': 'siemens',
             'SeriesDescription': ['t1'],
             'ExclusionStrings':['gad', 'gd'],
             'ImageType':['projection','derived'],
             'MRAcquisitionType': '3d',
             'ScanningSequence': ['gr']},

            {'Modality': 'mr',
             'Manufacturer': 'siemens',
             'SeriesDescription': ['mprage'],
             'ExclusionStrings':['gad', 'gd'],
             'ImageType':['projection','derived'],
             'MRAcquisitionType': '3d',
             'ScanningSequence': ['gr']},

            {'Modality': 'mr',
             'Manufacturer': 'ge',
             'SeriesDescription': ['t1'],
             'ExclusionStrings':['gad', 'gd'],
             'ImageType':['projection','derived'],
             'PulseSequenceName': 'bravo',
             'MRAcquisitionType': '3d',
             'ScanningSequence': ['gr']}
        ]
        list_files = []
        diff_keys = ['SeriesDescription', 'ScanningSequence', 'ImageType',
                     'InversionTime', 'ExclusionStrings', 'PulseSequenceName',
                     'PulseSequenceDetails', 'Manufacturer', 'SequenceName',
                     'SequenceVariant']

        for index, row in json_metadata.iterrows():
            data_lower = {key: value.lower() if isinstance(value, str) else value \
                          for key, value in row.items()}

            for criteria in criteria_combinations:
                criteria_values = []
                criteria_keys = set(criteria.keys()) - {'ExclusionStrings'}
                # First check if all the value from criteria are in data
                if all(key in data_lower.keys() for key in criteria_keys):
                    for key in criteria.keys():
                        if key not in diff_keys:
                            criteria_values.append(self.check_general(
                                data_lower[key], criteria[key]))

                        elif key in ['PulseSequenceName',
                                     'PulseSequenceDetails', 'Manufacturer',
                                     'SequenceName', 'SequenceVariant']:
                            criteria_values.append(self.check_contain_in_data(
                                data_lower[key], criteria[key]))

                        elif key == 'SeriesDescription':
                            exc_strings = criteria['ExclusionStrings'] \
                                if 'ExclusionStrings' in criteria.keys() else []
                            res_value = self.check_series_description(
                                data_lower[key], criteria[key], exc_strings)
                            criteria_values.append(res_value)

                        elif key == 'ScanningSequence':
                            criteria_values.append(self.check_scanning_sequence(
                                data_lower[key], criteria[key]))

                        elif key == 'ImageType':
                            # Criteria values must not be present in the
                            # ImageType field
                            criteria_values.append(self.check_image_type(
                                data_lower[key], criteria[key]))

                        elif key == 'InversionTime':
                            criteria_values.append(self.check_inversion_time_t1
                                                   (data_lower[key],
                                                    criteria[key]))

                if criteria_values and all(criteria_values):
                    file_name = row['json_file_path'] \
                        if row['json_file_path'] not in list_files else None
                    if file_name is not None:
                        list_files.append(file_name)

        return list_files

    def find_flair(self, json_metadata):
        """Among all MRI NIfTI sequences detect Flair ones"""

        criteria_combinations = [
            {'Modality': 'mr',
             'Manufacturer': 'philips',
             'SeriesDescription': ['flair'],
             'ExclusionStrings':['hipo', 'mip', '1nsa'],
             'PulseSequenceName': 'tir',
             'ScanningSequence': ['ir'],
             'ImageType':['projection','derived']},

            {'Modality': 'mr',
             'Manufacturer': 'philips',
             'SeriesDescription': ['flr'],
             'ExclusionStrings':['hipo', 'mip', '1nsa'],
             'PulseSequenceName': 'tir',
             'ScanningSequence': ['ir'],
             'ImageType':['projection','derived']},

            {'Modality': 'mr',
             'Manufacturer': 'philips',
             'SeriesDescription': ['flair'],
             'ExclusionStrings':['hipo', 'mip', '1nsa'],
             'ScanningSequence': ['ir'],
             'ImageType':['projection','derived']},

            {'Modality': 'mr',
             'Manufacturer': 'philips',
             'SeriesDescription': ['flr'],
             'ExclusionStrings':['hipo', 'mip', '1nsa'],
             'ScanningSequence': ['ir'],
             'ImageType':['projection','derived']},

            {'Modality': 'mr',
             'Manufacturer': 'siemens',
             'SeriesDescription': ['flair'],
             'ExclusionStrings':['hipo', 'mip', '1nsa'],
             'PulseSequenceDetails': 'tse',
             'ScanningSequence': ['se\ir'],
             'ImageType':['projection','derived']},

            {'Modality': 'mr',
             'Manufacturer': 'siemens',
             'SeriesDescription': ['flr'],
             'ExclusionStrings':['hipo', 'mip', '1nsa'],
             'PulseSequenceDetails': 'tse',
             'ScanningSequence': ['se\ir'],
             'ImageType':['projection','derived']},

            {'Modality': 'mr',
             'Manufacturer': 'siemens',
             'SeriesDescription': ['dark-fluid'],
             'ExclusionStrings':['hipo', 'mip', '1nsa'],
             'PulseSequenceDetails': 'tse',
             'ScanningSequence': ['se'],
             'ImageType':['projection','derived']},

            {'Modality': 'mr',
             'Manufacturer': 'ge',
             'SeriesDescription': ['flair'],
             'ExclusionStrings':['hipo', 'mip', '1nsa'],
             'PulseSequenceName': 't2flair',
             'ScanningSequence': ['se'],
             'ImageType':['projection','derived']},

            {'Modality': 'mr',
             'SeriesDescription': ['flair'],
             'ExclusionStrings':['stir', 'mra'],
             'InversionTime': 1},

            {'Modality': 'mr',
             'SeriesDescription': ['t2', 'dark'],
             'ExclusionStrings':['stir', 'mra'],
             'InversionTime': 1},

            {'Modality': 'mr',
             'SeriesDescription': ['t2', 'da', 'fl'],
             'ExclusionStrings':['stir', 'mra'],
             'InversionTime': 1},

            {'Modality': 'mr',
             'SeriesDescription': ['flr'],
             'ExclusionStrings':['stir', 'mra'],
             'InversionTime': 1}

        ]
        list_files = []
        diff_keys = ['SeriesDescription', 'ScanningSequence', 'ImageType',
                     'InversionTime', 'ExclusionStrings', 'PulseSequenceName',
                     'PulseSequenceDetails', 'Manufacturer', 'SequenceName',
                     'SequenceVariant']

        for index, row in json_metadata.iterrows():
            data_lower = {key: value.lower() if isinstance(value, str) else value \
                          for key, value in row.items()}

            for criteria in criteria_combinations:
                criteria_values = []
                criteria_keys = set(criteria.keys()) - {'ExclusionStrings'}
                # First check if all the value from criteria are in data
                if all(key in data_lower.keys() for key in criteria_keys):
                    for key in criteria.keys():
                        if key not in diff_keys:
                            criteria_values.append(self.check_general(
                                data_lower[key], criteria[key]))

                        elif key in ['PulseSequenceName',
                                     'PulseSequenceDetails', 'Manufacturer',
                                     'SequenceName', 'SequenceVariant']:
                            criteria_values.append(self.check_contain_in_data(
                                data_lower[key], criteria[key]))

                        elif key == 'SeriesDescription':
                            exc_strings = criteria['ExclusionStrings'] \
                                if 'ExclusionStrings' in criteria.keys() else []
                            res_value = self.check_series_description(
                                data_lower[key], criteria[key], exc_strings)
                            criteria_values.append(res_value)

                        elif key == 'ScanningSequence':
                            criteria_values.append(self.check_scanning_sequence(
                                data_lower[key], criteria[key]))

                        elif key == 'ImageType':
                            # Criteria values for this field must not be present
                            # in the data of the file
                            criteria_values.append(self.check_image_type(
                                data_lower[key], criteria[key]))

                        elif key == 'InversionTime':
                            criteria_values.append(self.check_inversion_time_flair(
                                data_lower[key],criteria[key]))

                if criteria_values and all(criteria_values):
                    file_name = row['json_file_path'] \
                        if row['json_file_path'] not in list_files else None
                    if file_name is not None:
                        list_files.append(file_name)

        return list_files

    def read_json_files(self, json_files_list):
        """Read json files to extract information needed to detect T1 or Flair
        sequence"""
        import pandas as pd
        import os
        import json

        df = pd.DataFrame()

        # Read each JSON file specified in the list
        for json_file_path in json_files_list:

            # Read the JSON file and convert to DataFrame
            with open(json_file_path, 'r') as json_file:
                json_data = json.load(json_file)
                json_df = pd.json_normalize(json_data)

                file_path,file_name=os.path.split(json_file_path)

                # Add a column with the folder path to identify the source
                json_df['folder_path'] = file_path
                json_df['file_name'] = file_name
                json_df['json_file_path'] = json_file_path

                # Concatenate with the main DataFrame
                df = pd.concat([df, json_df], ignore_index=True)

        df.fillna('', inplace=True)

        return df

    def convert_dicom_to_nifti(self, dcmfolder):
        """Convert DICOM files into NIfTI files"""

        import os
        import pydicom

        print("Converting dicom to nifti...")
        for kk in os.listdir(dcmfolder):
            # Avoid non-dicom files within folder
            try:
                idcm = os.path.join(dcmfolder,kk)
                dcm = pydicom.dcmread(idcm)
                break
            except:
                continue

        print(".  Using dicom: "+idcm)

        try: # convert original DICOM file into NIfTI file
            cmd = 'dcm2niix ' + str(dcmfolder)
            self.run_cmd(cmd, "Error converting dicom to nifti file")

        except: # in case of specific DICOM it needs to be first converted into
            # new DICOM file with gdcmconv tool and then continue with
            # conversion into NIfTI file

            out_folder = os.path.join(dcmfolder, 'gdcm_convert')
            for fn in os.listdir(dcmfolder):
                if not os.path.exists(out_folder):
                    os.makedirs(out_folder)
                idcm = os.path.join(dcmfolder, fn)
                odcm = os.path.join(out_folder, fn + "_gdcm")

                # convert DICOM to DICOM file
                cmd_gdcmconv = f"gdcmconv --jpeg {idcm} {odcm}"
                self.run_cmd(cmd_gdcmconv,
                             "Error converting dicom to dicom file")

            # converted DICOMs convert to NIfTI
            cmd_dcm2niix = f'dcm2niix -o {dcmfolder} {odcm}'
            self.run_cmd(cmd_dcm2niix,
                         "Error converting gdcm dicom to nifti file")

    def run_mideface(self, t1w_files_to_deface, outdir):
        """Perform defacing on the NIfTI T1 files. Mideface algorithm from
        Freesurfer is used for defacing"""

        import os
        import shutil

        fshome = "mescobrad_edge/plugins/mri_anonymisation_plugin/mideface/freesurfer"
        subjects_dir = "mescobrad_edge/plugins/mri_anonymisation_plugin/deface_files/"
        mideface_path = "mescobrad_edge/plugins/mri_anonymisation_plugin/mideface/freesurfer/bin/mideface"

        for filename_json in t1w_files_to_deface:

            # Find full path to the json file
            dcmfolder, file = os.path.split(filename_json)

            # Find full path to the NIfTI file
            basename = os.path.splitext(file)[0]
            file_path_nii = os.path.join(dcmfolder, f'{basename}.nii')

            outfile_mgz = os.path.join(dcmfolder, f'{basename}.mgz')
            outfile_defaced_mgz = os.path.join(outdir,
                                               f'{basename}_defaced.mgz')
            outfile_defaced_nifti = os.path.join(outdir, 'tmpdeface/T1',
                                                 f'{basename}.nii')
            qa = os.path.join(outdir, 'qa')

            print(" Defacing... \n")

            # Run the mideface algorithm
            # a) Set Freesurfer path
            # b) Run setup script
            # c) Set path to the data directory
            # d) Convert nifti to mgz format required for mideface
            # e) Run mideface algorithm
            # f) Convert output mgz to nifti

            cmd = f"export FREESURFER_HOME={fshome}" \
                + " && source $FREESURFER_HOME/SetUpFreeSurfer.sh" \
                + f" && export SUBJECTS_DIR={subjects_dir}" \
                + f" && mri_convert {file_path_nii} {outfile_mgz}" \
                + f" && {mideface_path} --i {outfile_mgz} --o {outfile_defaced_mgz} --odir {qa}" \
                + f" && mri_convert {outfile_defaced_mgz} {outfile_defaced_nifti}"

            self.run_cmd(cmd,"Error DeFaceing image")

            # Copy corresponding json file in the same folder
            destination_path = os.path.join(outdir, 'tmpdeface/T1')

            shutil.copy(filename_json, destination_path)

            print('======= Done defacing MRI data. =======')

    def copy_flair_files(self, flair_files_to_copy, outdir):
        """Move FLAIR files into the same folder where deface NIfTI T1 files
        are stored"""

        import os
        import shutil

        destination_path = os.path.join(outdir, 'tmpdeface/Flair')

        # - Create outfolder
        os.makedirs(destination_path, exist_ok = True)

        for flair_file_path_json in flair_files_to_copy:
            dcmfolder, file = \
                os.path.split(flair_file_path_json)
            flair_file_basename = os.path.splitext(file)[0]

            flair_file_path = os.path.join(dcmfolder, flair_file_basename)
            flair_file_path_nii = f'{flair_file_path}.nii'
            shutil.copy(flair_file_path_nii, destination_path)
            shutil.copy(flair_file_path_json, destination_path)


    def download_file(self, file_name: str, path_zip_file: str,
                      path_to_unzip: str) -> None:
        import boto3
        from botocore.client import Config
        import zipfile
        import os

        s3_local = boto3.resource('s3',
                                  endpoint_url=self.__OBJ_STORAGE_URL_LOCAL__,
                                  aws_access_key_id=\
                                    self.__OBJ_STORAGE_ACCESS_ID_LOCAL__,
                                  aws_secret_access_key=\
                                    self.__OBJ_STORAGE_ACCESS_SECRET_LOCAL__,
                                  config=Config(signature_version='s3v4'),
                                  region_name=self.__OBJ_STORAGE_REGION__)

        s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__)\
            .download_file(file_name, path_zip_file)

        # Delete original file in local storage
        s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__).\
            objects.filter(Prefix=file_name).delete()

        with zipfile.ZipFile(path_zip_file, 'r') as zip_ref:
            zip_ref.extractall(path_to_unzip)

        # After extraction delete downloaded zip file
        os.remove(path_zip_file)

    def create_pseudoMRN(self, mrn, workspace_id):
        import hashlib

        if mrn is None or workspace_id is None:
            pseudoMRN = None
        else:
            personalMRN = [mrn, workspace_id]
            personal_mrn = "".join(str(data) for data in personalMRN)

            # Generate ID
            pseudoMRN = hashlib.sha256(bytes(personal_mrn, "utf-8")).hexdigest()

        return pseudoMRN

    def update_filename_pid_mapping(self, obj_name, personal_id, pseudoMRN, mrn,
                                    s3_local):
        import csv
        import io

        folder = "file_pid/"
        filename = "filename_pid.csv"
        file_path = f"{folder}{filename}"

        bucket_local = s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__)
        obj_files = bucket_local.objects.filter(Prefix=folder, Delimiter="/")

        if (len(list(obj_files))) > 0:
            existing_object = \
                s3_local.Object(self.__OBJ_STORAGE_BUCKET_LOCAL__, file_path)
            existing_data = existing_object.get()["Body"].read().decode('utf-8')
            data_to_append = [obj_name, personal_id, pseudoMRN, mrn]
            existing_rows = list(csv.reader(io.StringIO(existing_data)))
            existing_rows.append(data_to_append)

            # Update column names
            column_names = ['filename', 'personal_id', 'pseudoMRN', 'MRN']
            if any(col_name not in existing_rows[0] for col_name in column_names):
                existing_rows[0] = column_names

            updated_data = io.StringIO()
            csv.writer(updated_data).writerows(existing_rows)
            s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__).upload_fileobj(
                io.BytesIO(updated_data.getvalue().encode('utf-8')), file_path)
        else:
            key_values = ['filename', 'personal_id', 'pseudoMRN', 'MRN']
            file_data = [key_values, [obj_name, personal_id, pseudoMRN, mrn]]
            updated_data = io.StringIO()
            csv.writer(updated_data).writerows(file_data)
            s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__).upload_fileobj(
                io.BytesIO(updated_data.getvalue().encode('utf-8')), file_path)

    def upload_file(self, path_to_anonymized_files: str, personal_id: str,
                    pseudoMRN: str, mrn: str) -> None:
        import boto3
        from botocore.client import Config
        import os
        from zipfile import ZipFile, ZIP_STORED
        import logging

        s3_local = boto3.resource('s3',
                                  endpoint_url=self.__OBJ_STORAGE_URL_LOCAL__,
                                  aws_access_key_id=\
                                    self.__OBJ_STORAGE_ACCESS_ID_LOCAL__,
                                  aws_secret_access_key=\
                                    self.__OBJ_STORAGE_ACCESS_SECRET_LOCAL__,
                                  config=Config(signature_version='s3v4'),
                                  region_name=self.__OBJ_STORAGE_REGION__)


        obj_name = os.path.split(path_to_anonymized_files)[1]
        zip_name = path_to_anonymized_files + "/" + obj_name + "_final.zip"

        # Create zip file with defaced and anonymized data
        files_exists = False
        with ZipFile(zip_name, 'w', ZIP_STORED) as zipObj:
            # Iterate over all the files in directory
            for root, dirs, files in os.walk(path_to_anonymized_files):
                for file in files:
                    if file.endswith('.nii'):
                        files_exists = True
                        # create complete filepath of file in directory
                        file_path = os.path.join(root, file)
                        basename_zip = os.path.basename(
                            path_to_anonymized_files)
                        second_part_of_zip_name = root.split(basename_zip)[1]
                        second_part_of_zip_name = \
                            second_part_of_zip_name.replace("tmpdeface/", "")
                        name_in_zipped_file = \
                            basename_zip + second_part_of_zip_name
                        name_in_zipped_file = os.path.join(name_in_zipped_file,
                                                           file)

                        # Add file to zip
                        zipObj.write(file_path, name_in_zipped_file,
                                     compress_type=ZIP_STORED)

                        # Add corresponding json file
                        file_path_json = os.path.splitext(file_path)[0] + ".json"
                        name_in_zipped_file_json = \
                            os.path.splitext(name_in_zipped_file)[0] + ".json"
                        zipObj.write(file_path_json, name_in_zipped_file_json,
                                     compress_type=ZIP_STORED)
                    else:
                        continue

        # Upload output zip file with defaced and anonymized data
        if files_exists:
            folder_name = "MRIs"
            name_of_file_minio = f"{folder_name}/{obj_name}.zip"
            try:
                s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__)\
                    .upload_file(zip_name, name_of_file_minio)
                print('======= File is uploaded to the local storage. =======')
            except Exception as e:
                os.remove(zip_name)
                logging.error(e)

            # Update key value file with mapping between filename and patient
            # id, this file is stored in the local MinIO instance
            self.update_filename_pid_mapping(name_of_file_minio, personal_id,
                                             pseudoMRN, mrn, s3_local)

        os.remove(zip_name)

        name_of_file = name_of_file_minio if files_exists else None
        return name_of_file

    def deidentify_files(self, path_to_files, outdir):
        """Iterate through data structure, and for each directory
        consisted of DICOM files perform defacing and anonymization."""

        import os
        import logging
        import shutil

        try:
            os.makedirs(outdir, exist_ok = True)
            for root, dirs, files in os.walk(path_to_files):
                if files: # check if there are files within current directory
                    # Remove all personal information
                    print(' Anonymization started ... \n')
                    self.annon_mri(path_to_defaced_files=os.path.join(root))

            # Convert to nifti files
            print(' Conversion to NiFTI files ... \n')
            dcmfolder = path_to_files
            self.convert_dicom_to_nifti(dcmfolder)

            print(' Extracting T1 and Flair sequences ... \n')
            # Extract all metadata to find appropriate T1 and Flair files
            # All corresponding json files
            all_json_files = []
            for root, dirs, files in os.walk(path_to_files):
                for file in files:
                    if file.endswith('.json'):
                        all_json_files.append(os.path.join(root, file))

            mri_metadata = self.read_json_files(all_json_files)

            # Extract T1 files
            t1w_files_to_deface = self.find_T1w(mri_metadata)

            # Extract FLAIR files
            flair_files = self.find_flair(mri_metadata)

            print(' T1 files which are detected and need to be defaced \n')
            print(t1w_files_to_deface)

            if t1w_files_to_deface:
                outdir_path = os.path.join(outdir, "defaced")
                # - Create outfolder
                os.makedirs(os.path.join(outdir,'defaced/tmpdeface/T1'),
                            exist_ok = True)
                self.run_mideface(t1w_files_to_deface, outdir_path)
                self.copy_flair_files(flair_files, outdir_path)
            else:
                print("--- T1 is not recognized within uploaded sequences. ---")

        except Exception as e:
            shutil.rmtree(outdir)
            logging.error(e ,"\n--- Impossible to deidentify files within " \
                          f"{path_to_files} folder ---")


    def generate_personal_id(self, personal_data):
        """Based on the identity, full_name and date of birth."""

        import hashlib

        personal_id = "".join(str(data) for data in personal_data)

        # Remove all whitespaces characters
        personal_id = "".join(personal_id.split())

        # Generate ID
        id = hashlib.sha256(bytes(personal_id, "utf-8")).hexdigest()
        return id

    def create_personal_identifier(self, data_info):
        import pandas as pd
        # Generate personal id
        if all(param is not None for param in [data_info['name'],
                                               data_info['surname'],
                                               data_info['date_of_birth'],
                                               data_info['unique_id']]):

            # Make unified dates, so that different formats of date doesn't
            # change the final id
            data_info["date_of_birth"] = pd.to_datetime(
                data_info["date_of_birth"], dayfirst=True)

            data_info["date_of_birth"] = \
                data_info["date_of_birth"].strftime("%d-%m-%Y")

            # Personal id is made based on name, surname, date date of birth,
            # and national unique id
            personal_data = [data_info["name"], data_info["surname"],
                             data_info["date_of_birth"], data_info["unique_id"]]

            personal_id = self.generate_personal_id(personal_data)
        else:
            # If the data is not provided set None value for the personal ID
            personal_id = None

        return personal_id

    def check_files_in_deideintifed_mri(self, path_zip_file):
        import zipfile

        # Check if the content of uploaded zip file is only consisted of .nii
        # and .json files
        allowed_files = {'.nii', '.json', '.NII', '.JSON'}

        with zipfile.ZipFile(path_zip_file, 'r') as zip_ref:
            # Get the list of all items in the ZIP archive
            for file_name in zip_ref.namelist():
                if not file_name.endswith('/'):
                    if not file_name.endswith(tuple(allowed_files)):
                        return False
        return True

    def upload_already_anonymized_and_defaced_mri(self, input_meta,
                                                  path_zip_file,
                                                  basename_without_ext):
        """If the uploaded data already anonymized and defaced, check the
        content and directly upload data on local and cloud object storage."""

        import boto3
        from botocore.client import Config
        import os

        # Download the file which needs to be uploaded
        s3_local = boto3.resource('s3',
                                  endpoint_url=self.__OBJ_STORAGE_URL_LOCAL__,
                                  aws_access_key_id=\
                                    self.__OBJ_STORAGE_ACCESS_ID_LOCAL__,
                                  aws_secret_access_key=\
                                    self.__OBJ_STORAGE_ACCESS_SECRET_LOCAL__,
                                  config=Config(signature_version='s3v4'),
                                  region_name=self.__OBJ_STORAGE_REGION__)

        file_name = input_meta.data_info['filename']
        s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__).download_file(
            file_name, path_zip_file)

        # Delete original file in local storage
        s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__).objects.filter(
            Prefix=file_name).delete()

        valid_files = self.check_files_in_deideintifed_mri(path_zip_file)

        if valid_files:
            # Create personal id
            personal_id = self.create_personal_identifier(input_meta.data_info)

            # Create pseudoMRN
            pseudoMRN = \
                self.create_pseudoMRN(input_meta.data_info["MRN"],
                                      input_meta.data_info['workspace_id'])

            # Upload output zip file with defaced and anonymized data
            folder_name = "MRIs"
            name_of_file_minio = f"{folder_name}/{basename_without_ext}.zip"
            s3_local.Bucket(self.__OBJ_STORAGE_BUCKET_LOCAL__).upload_file(
                path_zip_file, name_of_file_minio)

            print('======= File is uploaded to the local storage. =======')

            # Update key value file with mapping between filename and patient
            # id, this file is stored in the local MinIO instance
            self.update_filename_pid_mapping(name_of_file_minio, personal_id,
                                             pseudoMRN,
                                             input_meta.data_info["MRN"],
                                             s3_local)

            # Remove data
            os.remove(path_zip_file)

        else:
            name_of_file_minio = None
            os.remove(path_zip_file)
            raise ValueError("ERROR: Uploaded file contains files other than .nii and .json files")

        return name_of_file_minio

    def action(self, input_meta: PluginExchangeMetadata = None) -> \
        PluginActionResponse:
        """Run defacing algorithm.
        Remove all personal metadata.
        """
        import os
        import logging
        import shutil

        try:
            # Path where original and defaced data will be stored during
            # defacing and anonymisation
            path_to_data = \
                "mescobrad_edge/plugins/mri_anonymisation_plugin/deface_files/"

            name_of_anonymized_files = None

            pseudoMRN = self.create_pseudoMRN(
                input_meta.data_info['MRN'],
                input_meta.data_info['workspace_id'])

            # File to process
            if pseudoMRN is not None:
                folder_path, basename_path = os.path.split(input_meta.data_info['filename'])
                file_name = f"{folder_path}/{pseudoMRN}_{basename_path}"
            else:
                file_name = input_meta.data_info['filename']

            # Path init
            path_to_zip_file = None
            path_to_unzip_file = None
            path_to_defaced_structure = None


            if input_meta.data_info["upload_anonymized_and_defaced_data"]:

                basename = os.path.basename(file_name)
                basename_without_ext, _ = \
                    os.path.splitext(os.path.splitext(basename)[0])
                path_to_zip_file = f'{path_to_data}{basename_without_ext}.zip'

                name_of_file = \
                    self.upload_already_anonymized_and_defaced_mri(
                        input_meta, path_to_zip_file, basename_without_ext)
                name_of_anonymized_files = name_of_file
            else:

                path_to_zip_file = path_to_data + os.path.basename(file_name)
                path_to_unzip_file = path_to_data + os.path.basename(file_name).split(".")[0]

                # Download data to process
                self.download_file(input_meta.data_info['filename'],
                                   path_to_zip_file,
                                   path_to_unzip_file)


                if os.path.isdir(path_to_unzip_file):
                    dir = os.path.basename(path_to_unzip_file)
                    path_to_defaced_structure = os.path.join(path_to_data,
                                                             "deidentified",
                                                             dir)

                    # Perform defacing and anonymisation of the DICOM files
                    self.deidentify_files(path_to_unzip_file,
                                          path_to_defaced_structure)

                    # Create personal id
                    personal_id = self.create_personal_identifier(
                        input_meta.data_info)

                    # Upload processed data
                    name_of_file = self.upload_file(
                        path_to_defaced_structure, personal_id, pseudoMRN,
                        input_meta.data_info['MRN'])

                    name_of_anonymized_files = name_of_file

        except Exception as e:
            logging.error(e)

        finally:
            if path_to_zip_file is not None \
                and os.path.exists(path_to_zip_file):
                os.remove(path_to_zip_file)
            if path_to_defaced_structure is not None \
                and os.path.exists(path_to_defaced_structure):
                shutil.rmtree(path_to_defaced_structure)
            if path_to_unzip_file is not None \
                and os.path.exists(path_to_unzip_file):
                shutil.rmtree(path_to_unzip_file)

        return PluginActionResponse(None, None, name_of_anonymized_files,
                                    input_meta.data_info)

