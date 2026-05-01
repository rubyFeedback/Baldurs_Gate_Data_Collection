#!/usr/bin/ruby -w
# Encoding: UTF-8
# frozen_string_literal: true
# ============================================================================ #
# === Games::BaldursGate::PrepareMod
#
# This class will download and package the BG2 mod files.
#
# Usage example:
#
#   Games::BaldursGate::PrepareMod.new(ARGV)
#
# ============================================================================ #
# require 'games/individual_games/baldurs_gate/prepare_mod/prepare_mod.rb'
# ============================================================================ #
require 'games/base/base.rb'

module Games

module BaldursGate

class PrepareMod < Base # === Games::BaldursGate::PrepareMod

  # ========================================================================= #
  # === FILE_DETAILED_MOD_INSTALLATION_INSTRUCTIONS
  #
  # This file will contain all installation-instructions for BG2 mods.
  # ========================================================================= #
  FILE_DETAILED_MOD_INSTALLATION_INSTRUCTIONS = "#{::Games.project_yaml_directory?}"\
    "games/baldurs_gate_2/detailed_mod_installation_instructions.yml"

  # ========================================================================= #
  # === FILE_WEIDU_EXE
  #
  # The local copy of the weidu .exe.
  # ========================================================================= #
  FILE_WEIDU_EXE = '/depot/games/Baldurs_Gate/mods/setup-foobar.exe'

  # ========================================================================= #
  # === initialize
  # ========================================================================= #
  def initialize(
      commandline_arguments = nil,
      run_already           = true
    )
    reset
    set_commandline_arguments(
      commandline_arguments
    )
    run if run_already
  end

  # ========================================================================= #
  # === reset                                                     (reset tag)
  # ========================================================================= #
  def reset
    super()
    infer_the_namespace
  end

  # ========================================================================= #
  # === run                                                         (run tag)
  # ========================================================================= #
  def run
    # ======================================================================= #
    # Need to load up the dataset for the installation-instructions next.
    # ======================================================================= #
    _ = FILE_DETAILED_MOD_INSTALLATION_INSTRUCTIONS
    if File.exist? _
      batch_prepare_all_mods_via_this_yaml_file(_)
    else # else notify the user that the .yml file at hand does not exist.
      opnn; no_file_exists_at(_)
    end
  end

  # ========================================================================= #
  # === message_the_directory_is_not_empty_thus_not_making_any_changes
  # ========================================================================= #
  def message_the_directory_is_not_empty_thus_not_making_any_changes
    erev 'The directory is not empty. Not making any changes,'
    erev 'thus assuming that everything is already fine.'
  end

  # ========================================================================= #
  # === batch_prepare_all_mods_via_this_yaml_file
  # ========================================================================= #
  def batch_prepare_all_mods_via_this_yaml_file(
      i, # ← This should be a local .yml file.
      log_dir = log_dir?+'baldur_gate/' # We use a subdirectory here.
    )
    if i and File.file?(i)
      # In this case we know the .yml file exists. So load it upt.
      # ===================================================================== #
      # Load up the files that are to be installed next:
      # ===================================================================== #
      dataset = YAML.load_file(i)
      ensure_that_the_log_directory_exists(log_dir)
      cd(log_dir) # We should now be in /home/x/temp/games/baldur_gate/.
      starting_directory = return_pwd
      index = 0
      # ===================================================================== #
      # Process all registered entries next - note that dataset is a Hash
      # that looks like this:
      #
      #   {EET_from_Gibberlings3:
      #   {"name_to_use" => "EET_from_Gibberlings3",
      #
      # ===================================================================== #
      dataset.each_pair {|name_of_the_mod_as_symbol, inner_hash| index += 1
        use_git_checkout = false # false by default
        cliner
        erev "#{index}) Processing #{steelblue(name_of_the_mod_as_symbol)}#{rev} "\
             "next, in #{sdir(return_pwd)}#{rev}:"
        name_to_use    = inner_hash['name_to_use']
        latest_version = inner_hash['latest_version']
        last_checked   = inner_hash['last_checked']
        real_name      = inner_hash['real_name']
        latest_release_at = inner_hash['latest_release_at'] # Not always needed.
        github         = inner_hash['github']
        if inner_hash.has_key?('use_git_checkout')
          use_git_checkout = inner_hash['use_git_checkout']
        end
        padded_index   = '%03d' % index  
        # =================================================================== #
        # Next we must find out which subdirectory name we should use.
        # =================================================================== #
        name_of_the_subdirectory =
          "#{padded_index}_#{name_to_use}_version_#{latest_version}_published_on_the_#{last_checked}/"
        erev 'Creating the directory '+sdir(name_of_the_subdirectory)+rev+' next.'
        mkdir(name_of_the_subdirectory)
        cd(name_of_the_subdirectory)
        erev 'The current working-directory is `'+"#{sdir(return_pwd)}#{rev}`."
        erev "Processing #{lightgreen(name_of_the_mod_as_symbol.to_s)}"\
             "#{rev} by checking the remote source next."
        if use_git_checkout
          if Dir.empty?(return_pwd)
            # This here should not be done if the directory already contains
            # data.
            cmd = "git clone #{github}"
            esystem(cmd) { :forestgreen }
          else
            message_the_directory_is_not_empty_thus_not_making_any_changes
          end
        else # this here is for non-github links, making use of 'latest_release_at'.
          if Dir.empty?(return_pwd)
            erev 'Downloading via wget next:'
            wget_command = "wget \"#{latest_release_at}\""
            e "  #{steelblue(wget_command)}"
            system(wget_command) # And run it here.
            # ================================================================ #
            # Next check for lava-mods - these have an URL such as:
            #
            #   https://downloads.weaselmods.net/download/tangled-oak-isle/?wpdmdl=317&refresh=69e5834e3006d1776649038
            #
            # ================================================================ #
            all_files = Dir['*']
            first = all_files.first
            # ================================================================ #
            # === Handle lava-mods next
            # ================================================================ #
            if first.start_with?('index.html?')
              name_of_the_subdirectory = name_of_the_subdirectory.dup
              name_of_the_subdirectory.chop!
              name_of_the_subdirectory << '.zip'
              erev 'This is assumed to be a lava-mod. Renaming it next to'
              erev "#{steelblue(name_of_the_subdirectory)}#{rev}."
              rename_file(first, name_of_the_subdirectory)
              erev 'Extracting this file next.'
              require 'roebe/actions/actions.rb'
              ::Roebe.actions(:extract, name_of_the_subdirectory)
            end
          else
            message_the_directory_is_not_empty_thus_not_making_any_changes
          end
        end
        # ================================================================= #
        # We may need to copy the weidu.exe file still. 
        # ================================================================= #
        erev 'Checking whether an .exe file exists.'
        # ================================================================= #
        # Find all .exe files therein:
        # ================================================================= #
        appropriate_target = Dir['*.exe']
        if appropriate_target and appropriate_target.respond_to?(:first)
          appropriate_target = appropriate_target.first
        end
        if appropriate_target.nil? or appropriate_target.empty?
          if File.file?(FILE_WEIDU_EXE)
            erev 'No .exe could be found, thus copying '+
                 sfile(FILE_WEIDU_EXE)
            copy_file(FILE_WEIDU_EXE, return_pwd)
            appropriate_target = Dir['*.exe'].first.to_s
            new_name = "setup-#{real_name}.exe"
            erev "Renaming it next to #{steelblue(new_name)}"\
                 "#{rev}. (at: #{File.absolute_path(new_name)})"
            rename_file(appropriate_target, new_name)
          else
            no_file_exists_at(FILE_WEIDU_EXE)
          end
        else
          e "At the least one .exe exists already. ("\
            "#{steelblue(appropriate_target.to_s)}#{rev})"
          e "Thus, not copying #{sfile(FILE_WEIDU_EXE)}#{rev}."
        end 
        cd(starting_directory) # And go back again.
      }
    else
      no_file_exists_at(i)
    end
  end; alias install_the_entries_from_this_yaml_file batch_prepare_all_mods_via_this_yaml_file # === install_the_entries_from_this_yaml_file

  # ========================================================================= #
  # === Games::BaldursGate::PrepareMod[]
  # ========================================================================= #
  def self.[](
      i = ARGV
    )
    new(i)
  end

end

# ============================================================================ #
# === Games::BaldursGate::InstallBaldursGate
# ============================================================================ #
InstallBaldursGate = PrepareMod # === InstallBaldursGate

end; end

if __FILE__ == $PROGRAM_NAME
  Games::BaldursGate::PrepareMod.new(ARGV)
end # PrepareMod
