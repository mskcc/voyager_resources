#!/usr/bin/env python

import os, sys, re, subprocess, argparse, string , tempfile

static_header = '''@HD	VN:1.4	SO:unsorted
@SQ	SN:1	LN:249250621	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:1b22b98cdeb4a9304cb5d48026a85128
@SQ	SN:2	LN:243199373	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:a0d9851da00400dec1098a9255ac712e
@SQ	SN:3	LN:198022430	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:fdfd811849cc2fadebc929bb925902e5
@SQ	SN:4	LN:191154276	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:23dccd106897542ad87d2765d28a19a1
@SQ	SN:5	LN:180915260	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:0740173db9ffd264d728f32784845cd7
@SQ	SN:6	LN:171115067	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:1d3a93a248d92a729ee764823acbbc6b
@SQ	SN:7	LN:159138663	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:618366e953d6aaad97dbe4777c29375e
@SQ	SN:8	LN:146364022	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:96f514a9929e410c6651697bded59aec
@SQ	SN:9	LN:141213431	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:3e273117f15e0a400f01055d9f393768
@SQ	SN:10	LN:135534747	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:988c28e000e84c26d552359af1ea2e1d
@SQ	SN:11	LN:135006516	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:98c59049a2df285c76ffb1c6db8f8b96
@SQ	SN:12	LN:133851895	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:51851ac0e1a115847ad36449b0015864
@SQ	SN:13	LN:115169878	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:283f8d7892baa81b510a015719ca7b0b
@SQ	SN:14	LN:107349540	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:98f3cae32b2a2e9524bc19813927542e
@SQ	SN:15	LN:102531392	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:e5645a794a8238215b2cd77acb95a078
@SQ	SN:16	LN:90354753	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:fc9b1a7b42b97a864f56b348b06095e6
@SQ	SN:17	LN:81195210	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:351f64d4f4f9ddd45b35336ad97aa6de
@SQ	SN:18	LN:78077248	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:b15d4b2d29dde9d3e4f93d1d0f2cbc9c
@SQ	SN:19	LN:59128983	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:1aacd71f30db8e561810913e0b72636d
@SQ	SN:20	LN:63025520	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:0dec9660ec1efaaf33281c0d5ea2560f
@SQ	SN:21	LN:48129895	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:2979a6085bfe28e3ad6f552f361ed74d
@SQ	SN:22	LN:51304566	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:a718acaa6135fdca8357d5bfe94211dd
@SQ	SN:X	LN:155270560	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:7e0e2e580297b7764e31dbc80c2540dd
@SQ	SN:Y	LN:59373566	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:1fa3474750af0948bdf97d5a0ee52e51
@SQ	SN:MT	LN:16569	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:c68f52674c9fb33aef52dcf399755519
@SQ	SN:GL000207.1	LN:4262	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:f3814841f1939d3ca19072d9e89f3fd7
@SQ	SN:GL000226.1	LN:15008	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:1c1b2cd1fccbc0a99b6a447fa24d1504
@SQ	SN:GL000229.1	LN:19913	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:d0f40ec87de311d8e715b52e4c7062e1
@SQ	SN:GL000231.1	LN:27386	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:ba8882ce3a1efa2080e5d29b956568a4
@SQ	SN:GL000210.1	LN:27682	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:851106a74238044126131ce2a8e5847c
@SQ	SN:GL000239.1	LN:33824	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:99795f15702caec4fa1c4e15f8a29c07
@SQ	SN:GL000235.1	LN:34474	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:118a25ca210cfbcdfb6c2ebb249f9680
@SQ	SN:GL000201.1	LN:36148	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:dfb7e7ec60ffdcb85cb359ea28454ee9
@SQ	SN:GL000247.1	LN:36422	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:7de00226bb7df1c57276ca6baabafd15
@SQ	SN:GL000245.1	LN:36651	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:89bc61960f37d94abf0df2d481ada0ec
@SQ	SN:GL000197.1	LN:37175	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:6f5efdd36643a9b8c8ccad6f2f1edc7b
@SQ	SN:GL000203.1	LN:37498	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:96358c325fe0e70bee73436e8bb14dbd
@SQ	SN:GL000246.1	LN:38154	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:e4afcd31912af9d9c2546acf1cb23af2
@SQ	SN:GL000249.1	LN:38502	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:1d78abec37c15fe29a275eb08d5af236
@SQ	SN:GL000196.1	LN:38914	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:d92206d1bb4c3b4019c43c0875c06dc0
@SQ	SN:GL000248.1	LN:39786	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:5a8e43bec9be36c7b49c84d585107776
@SQ	SN:GL000244.1	LN:39929	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:0996b4475f353ca98bacb756ac479140
@SQ	SN:GL000238.1	LN:39939	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:131b1efc3270cc838686b54e7c34b17b
@SQ	SN:GL000202.1	LN:40103	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:06cbf126247d89664a4faebad130fe9c
@SQ	SN:GL000234.1	LN:40531	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:93f998536b61a56fd0ff47322a911d4b
@SQ	SN:GL000232.1	LN:40652	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:3e06b6741061ad93a8587531307057d8
@SQ	SN:GL000206.1	LN:41001	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:43f69e423533e948bfae5ce1d45bd3f1
@SQ	SN:GL000240.1	LN:41933	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:445a86173da9f237d7bcf41c6cb8cc62
@SQ	SN:GL000236.1	LN:41934	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:fdcd739913efa1fdc64b6c0cd7016779
@SQ	SN:GL000241.1	LN:42152	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:ef4258cdc5a45c206cea8fc3e1d858cf
@SQ	SN:GL000243.1	LN:43341	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:cc34279a7e353136741c9fce79bc4396
@SQ	SN:GL000242.1	LN:43523	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:2f8694fc47576bc81b5fe9e7de0ba49e
@SQ	SN:GL000230.1	LN:43691	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:b4eb71ee878d3706246b7c1dbef69299
@SQ	SN:GL000237.1	LN:45867	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:e0c82e7751df73f4f6d0ed30cdc853c0
@SQ	SN:GL000233.1	LN:45941	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:7fed60298a8d62ff808b74b6ce820001
@SQ	SN:GL000204.1	LN:81310	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:efc49c871536fa8d79cb0a06fa739722
@SQ	SN:GL000198.1	LN:90085	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:868e7784040da90d900d2d1b667a1383
@SQ	SN:GL000208.1	LN:92689	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:aa81be49bf3fe63a79bdc6a6f279abf6
@SQ	SN:GL000191.1	LN:106433	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:d75b436f50a8214ee9c2a51d30b2c2cc
@SQ	SN:GL000227.1	LN:128374	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:a4aead23f8053f2655e468bcc6ecdceb
@SQ	SN:GL000228.1	LN:129120	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:c5a17c97e2c1a0b6a9cc5a6b064b714f
@SQ	SN:GL000214.1	LN:137718	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:46c2032c37f2ed899eb41c0473319a69
@SQ	SN:GL000221.1	LN:155397	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:3238fb74ea87ae857f9c7508d315babb
@SQ	SN:GL000209.1	LN:159169	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:f40598e2a5a6b26e84a3775e0d1e2c81
@SQ	SN:GL000218.1	LN:161147	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:1d708b54644c26c7e01c2dad5426d38c
@SQ	SN:GL000220.1	LN:161802	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:fc35de963c57bf7648429e6454f1c9db
@SQ	SN:GL000213.1	LN:164239	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:9d424fdcc98866650b58f004080a992a
@SQ	SN:GL000211.1	LN:166566	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:7daaa45c66b288847b9b32b964e623d3
@SQ	SN:GL000199.1	LN:169874	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:569af3b73522fab4b40995ae4944e78e
@SQ	SN:GL000217.1	LN:172149	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:6d243e18dea1945fb7f2517615b8f52e
@SQ	SN:GL000216.1	LN:172294	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:642a232d91c486ac339263820aef7fe0
@SQ	SN:GL000215.1	LN:172545	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:5eb3b418480ae67a997957c909375a73
@SQ	SN:GL000205.1	LN:174588	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:d22441398d99caf673e9afb9a1908ec5
@SQ	SN:GL000219.1	LN:179198	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:f977edd13bac459cb2ed4a5457dba1b3
@SQ	SN:GL000224.1	LN:179693	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:d5b2fc04f6b41b212a4198a07f450e20
@SQ	SN:GL000223.1	LN:180455	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:399dfa03bf32022ab52a846f7ca35b30
@SQ	SN:GL000195.1	LN:182896	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:5d9ec007868d517e73543b005ba48535
@SQ	SN:GL000212.1	LN:186858	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:563531689f3dbd691331fd6c5730a88b
@SQ	SN:GL000222.1	LN:186861	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:6fe9abac455169f50470f5a6b01d0f59
@SQ	SN:GL000200.1	LN:187035	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:75e4c8d17cd4addf3917d1703cacaf25
@SQ	SN:GL000193.1	LN:189789	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:dbb6e8ece0b5de29da56601613007c2a
@SQ	SN:GL000194.1	LN:191469	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:6ac8f815bf8e845bb3031b73f812c012
@SQ	SN:GL000225.1	LN:211173	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:63945c3e6962f28ffd469719a747e73c
@SQ	SN:GL000192.1	LN:547496	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:325ba9e808f669dfeee210fdd7b470ac
@SQ	SN:NC_007605	LN:171823	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:6743bd63b3ff2b5b8985d8933c53290a
@SQ	SN:hs37d5	LN:35477943	UR:file:/ifs/depot/pi/resources/genomes/GRCh37/fasta/b37.fasta	M5:5b6a4b3a81a2d3c134b7d14bf6ad39f1
'''

def main(baits_ilist, targets_ilist, targets_name):
    fixedseq_report = dict()
    final_files = dict()
    rootpath = os.path.dirname(os.path.realpath(__file__))
    new_file_path = os.path.join(rootpath, format_filename(targets_name), "b37", "")
    for (ilist, ilist_type) in [(baits_ilist, "baits"), (targets_ilist, "targets")]:
        fh = open(ilist, "r")
        header = []
        body  = []
        while(True):
            line = fh.readline()
            if not line:
                break
            if line[0]=="@":
                header.append(line)
            else:
                body.append(line)
        header = static_header
        (fixed_body, fixedseq) = fix_body(body)
        fixedseq_report.update(fixedseq)
        try:
            os.makedirs(new_file_path)
        except OSError as e:
            if e.errno == 17:
                #already created, this is fine
                pass
        #FIXME hardcode b37 for now
        new_ilist_filename = format_filename(targets_name) + "_b37_" + ilist_type + ".ilist"
        full_path = os.path.join(new_file_path, new_ilist_filename)
        fh = open(full_path, "w")
        fh.write(header)
        fh.write("".join(body))
        fh.close()
        final_files[ilist_type]=full_path
        #now create FP snps for this automatically
    baits_bed = ilist2bed(final_files['baits'])
    targets_bed = ilist2bed(final_files['targets'])
    #FIXME hardcode this file from local space for now
    exac_file = "/ifs/res/pwg/data/exac/ExAC.r0.3.sites.pass.minus_somatic.vcf.gz"
    #tempfile for first command
    tempfh = tempfile.NamedTemporaryFile()
    tempfilename = tempfh.name
    tempfh.close()
    #final FP_intervals location
    fingerprint_vcf = os.path.join(new_file_path, format_filename(targets_name)+ "_fingerprint_snps.vcf")
    #get the snps of certain heterozygous freqeuency in our targets and put them in temp file
    cmd = ["bcftools", "filter", "--regions-file", targets_bed,
            "--include",
            "'GQ_MEAN>200 & Het_AFR>1561 & Het_AMR>1737 & Het_EAS>1298 & Het_FIN>992 & Het_NFE>10011 & Het_SAS>2477 & Het_OTH>136'",
            exac_file, "|", "bcftools", "view", "--exclude-types", "indels,mnps,other", "--output-file", tempfilename]
    execute_shell(cmd)
    #split mnps and exclude AF<0.1
    cmd2 = ["vt", "decompose", "-s", tempfilename, "|", "bcftools", "filter", "--exclude", "'AF<0.1'", "--output",
            fingerprint_vcf]
    execute_shell(cmd2)
    #create input formatted for analyzeFingerprints.py
    fp_tiling_genotypes = os.path.join(new_file_path, format_filename(targets_name) + "_FP_tiling_genotypes.txt")
    cmd3 = ["bcftools", "query", "-f",
            "'%CHROM:%POS\t%REF/%ALT\n'",
            fingerprint_vcf, ">", fp_tiling_genotypes]
    execute_shell(cmd3)
    print >>sys.stderr ,"#######CONVERSION SUMMARY##########"
    print >>sys.stderr, "Fixed chromosome names output in baits and targets:"
    for chrom in fixedseq_report.keys():
        print >>sys.stderr, "%s" % chrom,
    print >>sys.stderr, "\n",
    #CREATE intervals file for GATK DoC
    create_intervals(fp_tiling_genotypes, new_file_path)
    print >>sys.stderr, "##################################"

def create_intervals(genotypes_file, root_dir):
    intervals_file = os.path.join(root_dir, genotypes_file.replace("genotypes.txt", "intervals.intervals"))
    genofh = open(genotypes_file, "r")
    outfh = open(intervals_file, "wb")
    lines =0
    while(True):
        line = genofh.readline()
        if not line:
            break
        lines+=1
        (chr_start, geno) = line.split("\t")
        (chr, start) = chr_start.split(":")
        #pad 3 basepair to not worry about off by 1 garbage in anything
        #FIXME
        #kinda lazy
        stop = int(start)+1
        start = int(start)-1
        outline = chr + ":" + str(start) + "-" + str(stop)
        outfh.write(outline + "\n")
    outfh.close()
    genofh.close()
    print >>sys.stderr, "Interval file and genotypes created:\n%s\n%s" % (intervals_file, genotypes_file)
    print >>sys.stderr, "Total fingerprint sites selected: %d" % lines
    return



def execute_shell(cmd):
    try:
        print >>sys.stderr, "Executing %s" % " ".join(cmd)
        subprocess.check_call(" ".join(cmd), shell=True)
    except:
        print >>sys.stderr, "Unexpected Error: %s", sys.exc_info()[0]
        sys.exit(1)


def ilist2bed(ilist):
    ilistfh = open(ilist, "r")
    bed_filename = ilist.replace(".ilist", ".bed")
    outfh = open(bed_filename, "wb")
    while(True):
        line = ilistfh.readline()
        if not line:
            break
        if line[0]=="@":
            continue
        (chr, start, _) = line.split("\t", 2)
        start = int(start) - 1
        line = "\t".join([chr, str(start),_])
        outfh.write(line.replace(":", "\t"))
    outfh.close()
    return bed_filename



def format_filename(s):
    """Take a string and return a valid filename constructed from the string.
Uses a whitelist approach: any characters not present in valid_chars are
removed. Also spaces are replaced with underscores.

Note: this method may produce invalid filenames such as ``, `.` or `..`
When I use this method I prepend a date string like '2009_01_15_19_46_32_'
and append a file extension like '.txt', so I avoid the potential of using
an invalid filename.

CHARRIS NOTE: https://gist.github.com/seanh/93666

"""
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ','_') # I don't like spaces in filenames.
    return filename

def fix_body(body):
    m_index = -1
    fixedseq_report = dict()
    for i,line in enumerate(body):
        seq, _ = line.split("\t", 1)
        fixedseq = seq.replace("chr", "")
        fixedseq_report[fixedseq]=1
        body[i]="\t".join([fixedseq, _])
        if fixedseq=="M":
            m_index = i
    if(m_index > -1):
        del body[m_index]
    return (body, fixedseq_report)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="normalize ilist files for use with b37")
    parser.add_argument("--baits-ilist", required=True)
    parser.add_argument("--targets-ilist", required=True)
    parser.add_argument("--targets-name", required=True, help="Supply the string which will name the directory where these files will be stored in roslin_resources")

    args = parser.parse_args()
    if not os.path.exists(args.baits_ilist):
        print >>sys.stderr, "This file doesn't exist: %s" % args.baits_ilist
        sys.exit(1)
    if not os.path.exists(args.targets_ilist):
        print >>sys.stderr, "This file doesn't exist: %s" % args.targets_ilist
        sys.exit(1)
    main(args.baits_ilist, args.targets_ilist, args.targets_name)
